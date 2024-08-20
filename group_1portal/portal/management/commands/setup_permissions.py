from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Set up user roles and permissions'

    def handle(self, *args, **kwargs):
        # Define roles and permissions
        roles_permissions = {
            'User': ['view_profile', 'view_event', 'add_post'],
            'Moderator': ['view_profile', 'view_event', 'add_post', 'edit_post'],
            'Admin': ['view_profile', 'view_event', 'add_post', 'edit_post', 'delete_post']
        }

        for role, perm_codenames in roles_permissions.items():
            role_group, created = Group.objects.get_or_create(name=role)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created group "{role}"'))

            for codename in perm_codenames:
                try:
                    perm = Permission.objects.get(codename=codename)
                    role_group.permissions.add(perm)
                    self.stdout.write(self.style.SUCCESS(f'Added permission "{codename}" to group "{role}"'))
                except Permission.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Permission "{codename}" does not exist'))
