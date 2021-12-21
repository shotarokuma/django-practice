import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sample.settings')
from django import setup
setup()
from ModelApp.models import Person

p = Person(
  first_name='Taro',last_name= 'sato',
  birthday='2000-01-09',email='aa@mail.com',
  salary= 1000, memo= "memo taro",web_site="https::www"
)
p = Person(
  first_name='Taro',last_name= 'sato',
  birthday='2000-01-09',email='aa@mail.com',
  salary= None, memo= "memo taro",web_site="https::www"
)
p = Person(
  first_name='Taro',last_name= 'sato',
  birthday='2000-01-09',email='aa@mail.com',
  salary= 1000, memo= "memo taro",web_site=""
)

# p.save()

Person.objects.create(
  first_name='Jiro',last_name= 'Ito',
  birthday='2000-05-09',email='bb@mail.com',
  salary= 1000, memo= "クラスメソッド実行",web_site=""
)

obj, created = Person.objects.get_or_create(
    first_name='Saburo', last_name='Ito',
    email='bb@mail.com',
    salary = 90000, memo='class method 実行', web_site=None
)

print(obj)
print(created)
