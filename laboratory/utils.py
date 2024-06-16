import subprocess
from django.conf import settings

def start_websockify(vm_id):
    base_port = settings.WEBSOCKIFY_BASE_PORT
    vm_base_port = settings.VM_BASE_PORT
     
    vm_host = "localhost"
    proxy_port = base_port + int(vm_id)  

    cmdwebsockify = [
        'websockify',
        f'{proxy_port}',
        f'{vm_host}:{vm_base_port+int(vm_id)}'
    ]
    print(cmdwebsockify)

    process = subprocess.Popen(cmdwebsockify, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cmdqemu = [
        'qemu-system-x86_64',
        '-vnc',
        f':{vm_id}'
        ]
    print(cmdqemu)
    process = subprocess.Popen(cmdqemu, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proxy_port