from django.db import models
from createCustomer.models import Customer
from customerPolicy.models import Policy
# Create your models here.


class PolicyAssociate(models.Model):
    # = models.AutoField(primary_key=True)
    CustId = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
    )

    PolicyId = models.ForeignKey(
        Policy,
        on_delete=models.CASCADE,
    )
