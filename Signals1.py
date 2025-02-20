# Question 1: By default, Django signals are executed synchronously.
# Proof:
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

def signal_handler(sender, instance, **kwargs):
    print("Signal started")
    time.sleep(5)
    print("Signal finished")

post_save.connect(signal_handler, sender=User)

user = User.objects.create(username="test_user")
print("User creation complete")  # This will wait for the signal to finish

