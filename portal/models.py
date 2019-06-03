from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime
from django.db.models.signals import post_save
from django.contrib.auth.models import User

USER_MODEL = User


def create_executive(instance, sender, *args, **kwargs):
    if not hasattr(instance, 'executive'):
        Executive.objects.create(user=instance)


post_save.connect(create_executive, sender=USER_MODEL)


class Executive(models.Model):
    user = models.OneToOneField(USER_MODEL, on_delete=models.PROTECT)

    first_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True)

    employee_id = models.CharField(max_length=12, blank=True)

    date_of_birth = models.DateField(blank=True, null=True)
    details = models.TextField(blank=True)

    def __str__(self):
        return self.user.__str__()

    @property
    def get_display_name(self):
        if self.first_name:
            return self.first_name
        else:
            return self.user.username

    @property
    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def get_employee_id(self):
        if self.employee_id:
            return self.employee_id
        else:
            return "Not entered yet"

    @property
    def get_age(self):
        return datetime.date.today() - self.date_of_birth



