from django.contrib.auth.models import AbstractUser


class LinksUser(AbstractUser):
    pass

    def __str__(self):
        return self.username
