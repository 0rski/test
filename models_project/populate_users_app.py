import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'models_project.settings')

import django
django.setup()

import random
from users.models import User
from faker import Faker

fakegen = Faker()
# topics = ['search', 'social', 'marketplace', 'news']

# def add_topic():
#     t = topics.objects.get_or_create(top_name=random.choice(topics))[0]
#     t.save()
#     return t

def populate(N=5):

    for entry in range(N):
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        user_entry = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]

if __name__ == '__main__':
    print("populating script")
    populate(20)
    print("populating complete")
