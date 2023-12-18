from django.db import models
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from . import models, mixins

# Create your views here.

class Library(ListView):
    model = models.Book
    template_name = "main/index.html"
    context_object_name = 'books'
    paginate_by = 8
    
    
    def get_queryset(self):
        
        queryset = models.Book.objects.all()
        
        # In case there are filters
        title_filter = self.request.GET.get('title')
        genre_filter = self.request.GET.get('genre')
        pages_filter = self.request.GET.get('pages')
     
        # Apply the filters
        filters = Q()
        
        if title_filter:
            filters &= Q(title__icontains=title_filter)
        if genre_filter:
            filters &= Q(genre=genre_filter)
        if pages_filter:
            filters &= Q(pages__lte=pages_filter)
            
        return queryset.filter(filters)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = models.Book.objects.all()
        context['genres'] = books.values_list('genre', flat=True).distinct().order_by('genre')
        return context
    
class BookDetail(DetailView):
    model = models.Book
    template_name = 'book_detail/book_detail.html'
    context_object_name = 'book'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Gets all the user lists in which this book exists
        book = self.get_object()
                
        # Displays all lists of the current user
        if self.request.user.is_authenticated:
            user_lists = models.List.objects.filter(user__pk=self.request.user.pk)
            lists_with_book = models.List.objects.filter(book=book)
            context['user_lists'] = user_lists
            context['lists_with_book'] = lists_with_book
          
        return context

@login_required  
def add_book_to_list(request, slug, book_pk):
    '''
    Allows a user to add any book to any of the user's lists
    '''
    user_lists = request.POST.getlist('lists')
    added_book = models.Book.objects.get(pk=book_pk)
    
    if user_lists:
        for user_list in user_lists:
            list = models.List.objects.get(name=user_list)
            if list.user.filter(pk=request.user.pk).exists():
                list.book.add(added_book)
            else:
                pass 
    return redirect('lists', username=request.user.username)

@login_required
def delete_book_from_list(request, username, slug, book_pk):
    list = models.List.objects.get(slug=slug)
    if list.user.filter(pk=request.user.pk).exists():
        book_to_remove = models.Book.objects.get(pk=book_pk)
        list.book.remove(book_to_remove)
        return redirect('list-detail', username=username, slug=slug)
    list_owner = list.user.first() if list.user.first() else "unknown"
    raise Http404(f"You cannot modify this list. This list belongs to {list_owner}")

class UserLists(LoginRequiredMixin, ListView):
    
    login_url = 'login'
    
    model = models.List
    template_name = 'user_lists/user_lists.html'
    context_object_name = 'lists'
    paginate_by = 8
    
    def get_queryset(self):
        # Only get the current logged user's lists
        queryset = models.List.objects.filter(user__pk=self.request.user.pk).order_by('created')
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Gets lists shared with the current user
        context['shared_lists'] = models.List.objects.filter(shared_to__contains=[self.request.user.username])
        
        # Displays all users 
        context['users'] = models.User.objects.exclude(is_staff=True).exclude(pk=self.request.user.pk)
        return context
    
class ListDetail(LoginRequiredMixin, DetailView):
    login_url = 'login'
    
    model = models.List
    template_name = 'user_lists/list_detail.html'
    context_object_name = 'list_details'   

class CreateList(LoginRequiredMixin, CreateView):
    
    login_url = 'login'
    
    model = models.List
    template_name = 'user_lists/create_list.html'
    fields = ['name', 'description']
    
    def form_valid(self, form):
        form.instance.save()
        form.instance.user.add(self.request.user)
        return super().form_valid(form)
    
    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('lists', kwargs={'username': username})
    
class DeleteList(LoginRequiredMixin, mixins.CheckOwnerMixin, DeleteView):
    login_url = 'login'
    
    model = models.List
    template_name = 'user_lists/delete_list.html'
    
    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('lists', kwargs={'username': username})
    
class UpdateList(LoginRequiredMixin, mixins.CheckOwnerMixin, UpdateView):
    login_url = 'login'
    
    model = models.List
    template_name = 'user_lists/update_list.html'
    fields = ['name', 'description', 'book']
    
    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('lists', kwargs={'username': username})
    
@login_required
def share_list(request, username, slug):
    '''
    This view allows the user to share lists with other users.
    '''
    
    share_to_user = request.POST.getlist('users')
    if share_to_user:
        list_to_share = models.List.objects.get(slug=slug)
        for user in share_to_user:
            list_to_share.shared_to.append(user)
            list_to_share.save()
    
    return redirect('lists', username=username)   