from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


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


class Player(AbstractBaseModel, AbstractUser):
    def __str__(self):
        return self.label()

    def label(self):
        full_name = ' '.join([s for s in [self.first_name, self.last_name] if s])
        return full_name or self.username
