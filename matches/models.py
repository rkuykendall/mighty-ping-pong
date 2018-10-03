from django.db import models

from base.models import AbstractBaseModel
from mighty_ping_pong import settings


class Match(AbstractBaseModel):
    winner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='matches_won',
        on_delete=models.CASCADE,
    )
    loser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='matches_lost',
        on_delete=models.CASCADE,
    )
