from django.urls import path

from . import views

urlpatterns = [
    path("labview", views.index, name="index"),
    path("create", views.create_vm_instance, name="create_vm_instance"),

]