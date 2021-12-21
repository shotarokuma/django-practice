import os

from pytz import country_names

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sample.settings')
from django import setup
setup()

from ModelApp.models import Students

print(Students.objects.all())

print(Students.objects.count())
print(Students.objects.filter(name = 'A').count())

from django.db.models import Count, Max, Min, Avg, Sum
# print(Students.objects.aggregate(Count('pk'),Max('pk'),Min('pk'),Avg('pk'),Sum('pk')))
aggregate_students = Students.objects.aggregate(Count('pk'),Max('pk'),Min('pk'),Avg('pk'),Sum('pk'))
print(aggregate_students['pk__count'])

print(Students.objects.values('name').annotate(
  Max('pk'),Min('pk')
))

