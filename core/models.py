from django.db import models
from  account.models import User

import uuid

# Create your models here.
TRANSACTION_TYPE = (
    ('Debit', 'Debit'), 
    ('Credit', 'Credit') 
)

class History(models.Model):
    user =  models.ForeignKey(User, related_name='history', on_delete=models.CASCADE) 
    account_number = models.CharField(max_length=100)
    transaction_type = models.CharField(choices=TRANSACTION_TYPE, default="Debit", max_length=10)
    amount = models.IntegerField()
    transaction_reference = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    date = models.DateField()