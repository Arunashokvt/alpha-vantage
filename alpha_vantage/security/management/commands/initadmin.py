import os
from django.conf import settings
from django.core.management import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        try:
            print('Creating super user..')
            if not User.objects.first():
                username = os.environ.get('ADMIN_USER_NAME')
                email = os.environ.get('ADMIN_EMAIL')
                password = os.environ.get('ADMIN_PASSWORD')
                print('Creating account for %s (%s)' % (username, email))
                admin = User.objects.create_superuser(email=email,
                                                      username=username,
                                                      password=password
                                                      )
                admin.is_active = True
                admin.is_admin = True
                admin.save()
            else:
                print('Admin accounts can only be initialized if no Accounts exist')
        except Exception as e:
            print(e)
            pass
