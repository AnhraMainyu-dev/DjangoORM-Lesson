import os
import django


from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
execute_from_command_line('manage.py runserver 0.0.0.0:8000'.split())
django.setup()

from datacenter.models import Visit, Passcard
passcode = '0cc28790-756b-4b3d-b5ef-b71c1d3e4302'
passcard = Passcard.objects.get(passcode=passcode)
visits = Visit.objects.filter(passcard=passcard)
print(visits)

