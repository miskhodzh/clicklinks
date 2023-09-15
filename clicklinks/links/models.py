from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Links(models.Model):
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='links'
        )
    link_name = models.CharField(max_length=100)
    link_url = models.URLField()

    def __str__(self) -> str:
        return self.link_name
