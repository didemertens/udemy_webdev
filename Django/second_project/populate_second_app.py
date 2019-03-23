import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','second_project.settings')

import django
django.setup()

## Fake pop script
from second_app.models import User
from faker import Faker

fake = Faker()

def populate(N=5):

  for i in range(N):

    # create fake data
    fake_first = fake.first_name()
    fake_last = fake.last_name()
    fake_mail = fake.email()

    user = User.objects.get_or_create(first_name=fake_first, last_name=fake_last, email=fake_mail)[0]

if __name__ == '__main__':
  print('populating script!')
  populate(10)
  print('populating complete')


