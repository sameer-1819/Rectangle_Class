# Question 3: Django signals run in the same database transaction as the caller.
# Proof:
from django.db import transaction

def signal_handler(sender, instance, **kwargs):
    print(f"Signal: user exists in DB? {User.objects.filter(id=instance.id).exists()}")

post_save.connect(signal_handler, sender=User)

with transaction.atomic():
    user = User.objects.create(username="test_user")
    print(f"Caller: user exists in DB? {User.objects.filter(id=user.id).exists()}")