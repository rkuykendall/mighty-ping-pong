from uuid import uuid4

from django.db import models
from django.conf import settings


class FriendlyNameMixin(object):
    @classmethod
    def get_friendly_model_name(cls) -> str:
        return cls._meta.db_table.lower()  # type: ignore

    @classmethod
    def slugify_model_name(cls) -> str:
        return cls.get_friendly_model_name().replace('_', '-')

    def type(self) -> str:
        return self._meta.label_lower  # type: ignore


class AbstractTimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True


class AbstractBaseModel(AbstractTimeStampedModel, FriendlyNameMixin):
    id = models.UUIDField(primary_key=True, default=uuid4)

    class Meta:
        abstract = True
        ordering = ['-created_at']


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
