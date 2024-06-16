from django.shortcuts import render , redirect
from .models import VMType, VMInstance
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .utils import start_websockify

@login_required
def index(request):
    user = request.user
    vm_instance = VMInstance.objects.filter(owner=user).first()
    if vm_instance:
        port = start_websockify(vm_instance.id, )
        context = {
            "port": port,
        }
        return render(request, "laboratory/noVNC.html", context)
    else:
        return redirect('create_vm_instance')





@login_required
def create_vm_instance(request):
    if request.method == 'POST':
        vm_type_id = request.POST.get('vm_type')
        vm_type = VMType.objects.get(id=vm_type_id)
        user = request.user

        # Get or create the VMInstance for the current user
        vm_instance, created = VMInstance.objects.get_or_create(
            owner=user,
            defaults={'vm_type': vm_type}
        )

        # If the VMInstance already exists, update the vm_type
        if not created:
            vm_instance.vm_type = vm_type
            vm_instance.save()

        # Redirect to the index view
        return redirect('index')

    # Get all available VMType instances
    vm_types = VMType.objects.all()

    return render(request, 'laboratory/create_vm_instance.html', {'vm_types': vm_types})