from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):

        if username is None:
            raise TypeError('username is required')

        if email is None:
            raise TypeError('email is required')

        user = self.model(username=username, email = self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user 

    def create_superuser(self, username, email, password):

        if password is None:
            raise TypeError('superuser must have a password')

        user = self.create_user(username, email, password)
        user.is_superuser = True 
        user.is_staff = True 
        user.save()

        return user 