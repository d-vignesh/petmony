from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _ 

import jwt
import uuid
from datetime import datetime, timedelta

from .managers import UserManager 

class User(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username + ' with email ' + self.email 

    @property 
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        """
            generates a json web token using this user's ID and an expiry date of 60 days
        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': str(self.pk),
            'email': self.email,
            'username': self.username,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

    def get_full_name(self):
        return self.username 

    def get_short_name(self):
        return self.username 
