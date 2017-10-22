from rest_framework import serializers
from .models import Recharge

class RechargeSerializer(serializers.ModelSerializer):

    class Meta:
        model=Recharge
        fields=('first_name','last_name','account_balance')