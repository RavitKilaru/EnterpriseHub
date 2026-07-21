from django.db import models


class BaseQuerySet(models.QuerySet):

    def active(self):
        return self.filter(is_active=True, is_deleted=False)

    def inactive(self):
        return self.filter(is_active=False, is_deleted=False)

    def deleted(self):
        return self.filter(is_deleted=True)

    def alive(self):
        return self.filter(is_deleted=False)