from rest_framework import serializers
from .models import PolicyAssociate



class PolicyAssociateSerializers(serializers.ModelSerializer):
    class Meta:
        model = PolicyAssociate
        fields = ("id","CustId","PolicyId")
