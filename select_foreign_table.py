import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sample.settings')
from django import setup
setup()

# from ModelApp.models import Schools,Students,Prefectures
# s = Schools.objects.first()
# # print(type(s))
# # print(dir(s))
# print(s.prefecture.name)
# st = s.students_set
# print(type(st))
# print(st.all())

# from ModelApp.models import Places, Restaurants
# p = Places.objects.first()
# print(p.restaurants.name)
# r = Restaurants.objects.first()
# print(r.place.name)

from ModelApp.models import Books, Authors
b = Books.objects.first()
print(b.authors.all())
r = Authors.objects.first()
print(r.books_set.all())

