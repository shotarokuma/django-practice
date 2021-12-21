import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Students, Schools

# for student in Students.objects.all():
#     print(student.name, student.school.name, student.school.prefecture.name)

# for student in Students.objects.filter(school__name='南高校'):
#     print(student.name, student.school.name, student.school.prefecture.name)

# for student in Students.objects.exclude(school__name='南高校'):
#     print(student.name, student.school.name, student.school.prefecture.name)

# print(Students.objects.filter(school__name='東高校').query)

for student in Students.objects.order_by('-school__name'):
    print(student.name, student.school.name)

from django.db.models import Count, Max, Sum
print(Students.objects.values('school__name').annotate(Count('id'), Max('id'), Sum('id')))
