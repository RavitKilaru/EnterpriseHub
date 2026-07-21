from django.db import models


class TimeStampMixin(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class StatusMixin(models.Model):

    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class SoftDeleteMixin(models.Model):

    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True