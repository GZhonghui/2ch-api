from django.db import models
from django.contrib.auth import get_user_model

# django.contrib.auth.models.User
User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    one_word = models.CharField(verbose_name="One Word", max_length=128, blank=True)

    class Meta:
        db_table = "user_profile_table"
