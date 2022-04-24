from django.db.models.signals import post_save
from django.contrib.auth.models import Group, User
from .models import Customer


def customer_profile(sender, instance, create, *args, **kwargs):
    if create:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)

        Customer.objects.create(
            user=instance,
            name=instance.username,
        )
        print('Profile created!')

post_save.connect(customer_profile, sender=User)


