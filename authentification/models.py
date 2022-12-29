from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    # username = None     # Nom utilisateur
    first_name = None   # prénom
    last_name = None    # nom de famille
    email = None        # email
    # password = None     # password
    is_staff = None     # utilisateur pouvant se connecter au site admin django
    is_active = False   # utilisateur actif
    is_superuser = None # obtention de toutes les permissions, telles que l'accès au site admin

    pass
