from django.http import Http404

class CheckOwnerMixin:
    def dispatch(self, request, *args, **kwargs):
        my_list = self.get_object()
        
        if my_list.user.filter(pk=request.user.pk).exists():
            return super().dispatch(request, *args, **kwargs)
        else:
            list_owner = my_list.user.first().username if my_list.user.first() else "unknown"
            raise Http404(f"You cannot modify this list. This list belongs to {list_owner}")
    