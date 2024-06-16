## About
Cette application est un outil convivial basé sur le web qui permet à n'importe qui de créer et d'interagir avec des machines virtuelles (VM) directement dans leur navigateur. Elle est conçue pour être simple et intuitive, même pour les utilisateurs sans connaissances techniques. L'application se compose de quatre pages principales :

    Page de Connexion/Inscription : C'est ici que les utilisateurs se connectent à leur compte existant ou créent un nouveau compte. Le processus est simple, ne nécessitant qu'un nom d'utilisateur, un mot de passe et peut-être une adresse e-mail. Une fois inscrits, les utilisateurs peuvent accéder à toutes les fonctionnalités de l'application.

    Page de Configuration : Sur cette page, les utilisateurs configurent leur machine virtuelle. Une machine virtuelle (VM) est comme un ordinateur dans un ordinateur; elle exécute son propre système d'exploitation et ses applications, séparément de l'ordinateur hôte. Les utilisateurs peuvent choisir le système d'exploitation (OS) qu'ils veulent installer sur leur VM, comme Windows, Linux ou d'autres options disponibles. Le processus de configuration est simplifié pour que les utilisateurs puissent facilement sélectionner leurs préférences sans avoir besoin de comprendre les détails techniques.

    Page de la Machine Virtuelle : C'est le cœur de l'application, où les utilisateurs interagissent avec leur machine virtuelle en temps réel. Une fois la VM configurée, les utilisateurs peuvent l'utiliser comme un ordinateur ordinaire. Ils peuvent ouvrir des applications, naviguer sur Internet et effectuer d'autres tâches. L'interface est conçue pour être réactive et intuitive, donnant l'impression qu'elle fait partie intégrante de leur expérience de navigation.

    Page du Tableau de Bord : Cette page optionnelle mais utile fournit un aperçu de toutes les machines virtuelles créées par un utilisateur. Elle permet aux utilisateurs de gérer leurs VM, de surveiller leur état, de les démarrer ou de les arrêter, et d'accéder à d'autres fonctionnalités administratives. Cela aide à tout organiser et rendre facilement accessible.

Pourquoi Cette Application est Utile

    Accessibilité : En étant basée sur le web, cette application peut être accessible depuis n'importe quel appareil avec une connexion internet et un navigateur. Il n'est pas nécessaire d'installer des logiciels supplémentaires sur l'appareil de l'utilisateur.

    Rentabilité : Les utilisateurs peuvent créer et exécuter des machines virtuelles sans avoir besoin d'investir dans du matériel physique. Cela est particulièrement bénéfique pour les utilisateurs qui ont besoin de plusieurs systèmes d'exploitation pour différentes tâches mais ne veulent pas acheter plusieurs ordinateurs.

    Apprentissage et Expérimentation : Les machines virtuelles sont excellentes pour l'apprentissage et l'expérimentation. Les utilisateurs peuvent essayer de nouveaux systèmes d'exploitation, logiciels ou configurations sans risquer leur ordinateur principal. Si quelque chose tourne mal, ils peuvent simplement réinitialiser la VM et recommencer.

    Isolation et Sécurité : Exécuter des applications dans une machine virtuelle peut améliorer la sécurité en les isolant du système d'exploitation principal. Cette isolation aide à protéger le système principal de l'utilisateur contre les logiciels malveillants ou autres problèmes pouvant survenir au sein de la VM.

En résumé, cette application web simplifie le processus de création et d'utilisation de machines virtuelles, rendant des capacités informatiques puissantes accessibles à tous, quelle que soit leur connaissance technique. Que ce soit pour l'éducation, le développement, les tests ou l'utilisation quotidienne, elle offre un environnement flexible et sécurisé pour les utilisateurs désireux d'explorer et d'innover.

## Prerequisites

1. **Git**: To clone the repository.
2. **Windows Subsystem for Linux (WSL)**: To run the Linux environment on Windows.
3. **QEMU-KVM**: For virtualization if needed.
4. **Python and Pip**: To run the Django application.
5. **Virtualenv**: For managing Python environments.

## WSL Installtion 
1. Open PowerShell as Admin
2. Run **wsl --install**
3. Reboot

## Installing qemu
1. Open PowerShell
2. Run **wsl** comande
3. Run **sudo apt install qemu-kvm**

## Installing the app
1. Run git clone https://github.com/User-0041/vLab.git
2. cd vLab
3. python3 -m venv venv
4. source venv/bin/activate
5. pip install -r requirements.txt
6. python manage.py migrate
7. python manage.py createsuperuser
8. python manage.py runserver