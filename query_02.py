import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sample.settings')
from django import setup
setup()

from ModelApp.models import Students, Person

# print(Students.objects.all())
ids = [13, 14, 15]
print(Students.objects.filter(pk__in=ids).all())

print(Students.objects.filter(name__contains='三').all())

p = Person(
    first_name='Jiro', last_name='Yamada',
    birthday='2000-01-01', email='aa@mail.com',
    salary=1000, memo='memo taro', web_site='http://www.google'
)
p.save()
print(Person.objects.filter(salary__isnull=True).all())
print(Person.objects.exclude(salary__isnull=True).all())

print(Students.objects.exclude(name='A').all())

print(Students.objects.values('name', 'age').all())

students = Students.objects.values('id', 'name', 'age').all()
for student in students:
    print(student['id'])


print(Students.objects.order_by('-name', 'id').all())