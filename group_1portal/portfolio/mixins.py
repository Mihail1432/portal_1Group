from django.contrib.auth.mixins import PermissionRequiredMixin

class UserIsOwner(PermissionRequiredMixin):
    def has_permission(self):
        return self.request.user == self.get_object().user