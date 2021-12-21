import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sample.settings')
from django import setup
setup()
from ModelApp.models import Person

persons = Person.objects.all()
for person in persons:
  print(person.id,person,person.salary)

# person = Person.objects.get(first_name ='Taro')
# person = Person.objects.get(first_name ='taro')

person = Person.objects.get(pk = 4)
print(person)
persons = Person.objects.filter(first_name='Taro').all()
print(persons[0])
for person in persons:
  print(person.id, person)






