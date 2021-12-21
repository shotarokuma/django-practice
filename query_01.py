import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sample.settings')
from django import setup
setup()

from ModelApp.models import Students

# print(Students.objects.all())

# print(Students.objects.all()[:5])

# print(Students.objects.all()[5:])

# print(Students.objects.all()[5:8])
# print(Students.objects.all()[5:8].query)

# print(Students.objects.first())

# print(Students.objects.filter(name='太郎').all())
# print(Students.objects.filter(age=17).all())

# print(Students.objects.filter(name='太郎', pk__gt=13).all().query)
# print(Students.objects.filter(name='太郎', pk__lt=20).all())
# print(Students.objects.filter(name='太郎', pk__gte=13, pk__lte=16).all().query)

# print(Students.objects.all())
# print(Students.objects.filter(name__startswith='太').all())

# print(Students.objects.filter(name__endswith='郎').all())

# or
# from django.db.models import Q
# print(Students.objects.filter(Q(name='太郎') | Q(pk__gt=19)).all())