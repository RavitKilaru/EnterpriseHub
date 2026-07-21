import uuid

from django.db import models

from .managers import BaseManager
from .mixins import (
    TimeStampMixin,
    StatusMixin,
    SoftDeleteMixin,
)


class BaseModel(
    TimeStampMixin,
    StatusMixin,
    SoftDeleteMixin,
):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    objects = BaseManager()

    class Meta:
        abstract = True

    def soft_delete(self):
        self.is_deleted = True
        self.save(update_fields=["is_deleted"])

    def restore(self):
        self.is_deleted = False
        self.save(update_fields=["is_deleted"])