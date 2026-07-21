"""
Application-wide constants and model choices.
"""

from django.db import models


class StatusChoices(models.TextChoices):
    ACTIVE = "ACTIVE", "Active"
    INACTIVE = "INACTIVE", "Inactive"


class DeleteStatusChoices(models.TextChoices):
    AVAILABLE = "AVAILABLE", "Available"
    DELETED = "DELETED", "Deleted"