from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class MagicLoginToken(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='magic_login_tokens',
    )
    token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)

    def is_valid(self):
        expiration_time = self.created_at + timedelta(minutes=15)
        return not self.used and timezone.now() <= expiration_time

    def __str__(self):
        return f"Magic token for {self.user.username}"
