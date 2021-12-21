import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sample.settings')
from django import setup
setup()

from ModelApp.models import Person

Person.objects.filter(first_name='Saburo').delete()
Person.objects.filter(first_name='taro' ,birthday ='2999-09-09').delete()

Person.objects.all().delete()
