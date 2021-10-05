import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "eterproject.settings")

import django
django.setup()

from populationapp.models import customuser


from faker import Faker

fake = Faker()
def fillcustomeruser(number = 100):
        for i in range(number):
            user = customuser.objects.get_or_create(
                first_name= fake.name(),
                last_name = fake.name(),
                email = fake.email(),
            )[0]

                
if __name__ == "__main__":
    fillcustomeruser(100)
