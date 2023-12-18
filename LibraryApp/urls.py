from django.urls import path
from . import views

urlpatterns = [
    path('', views.Library.as_view(), name='index'),
    path('detail/<slug:slug>', views.BookDetail.as_view(), name='book-detail'),
    path('detail/<slug:slug>/add/<str:book_pk>', views.add_book_to_list, name='add-book'),
    path('<str:username>/lists', views.UserLists.as_view(), name='lists'),
    path('<str:username>/lists/create', views.CreateList.as_view(), name='list-create'),
    path('<str:username>/lists/delete/<slug:slug>', views.DeleteList.as_view(), name='list-delete'),
    path('<str:username>/lists/update/<slug:slug>', views.UpdateList.as_view(), name='list-update'),
    path('<str:username>/lists/share/<slug:slug>', views.share_list, name='list-share'),
    path('<str:username>/lists/<slug:slug>', views.ListDetail.as_view(), name='list-detail'),
    path('<str:username>/lists/<slug:slug>/delete/<str:book_pk>', views.delete_book_from_list, name='delete-book'),
]