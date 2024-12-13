from django.contrib.auth.mixins import AccessMixin

class UserIsStaffMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return self.handle_no_permission()
        
        return super().dispatch(request, *args, **kwargs)
    

class UserHasNotCompletedMixin(AccessMixin):
    permission_denied_message = "You have already completed this."


    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        if self.request.user in obj.get_users_that_completed():
            return self.handle_no_permission()

        return super().dispatch(request, *args, **kwargs)