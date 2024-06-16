from django.db import models
from django.contrib.auth.models import User

class VMType(models.Model):
    name = models.CharField(max_length=100)
    iso_path = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class VMInstance(models.Model):
    vm_type = models.ForeignKey(VMType, on_delete=models.CASCADE)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vm_instance')
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.vm_type.name} (owned by {self.owner.username})"