from django.contrib.auth.management.commands import createsuperuser
from ...models import mUser

class Command(createsuperuser.Command):
    help = 'Create a Superuser'

    def handle(self, *args, **options):
        options.setdefault('interactive', False)
        username = 'admin'
        email = 'admin@gmail.com'
        password = 'admin'
        database = options.get('database')

        user_data = {
            'username': username,
            'email': email,
            'password': password,
        }

        exists = self.UserModel._default_manager.db_manager(database).filter(username=username).exists()
        if not exists:
            self.UserModel._default_manager.db_manager(database).create_superuser(**user_data)
        
