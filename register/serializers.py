from rest_framework import serializers

from .models import MicroApp
from .models import Transaction

class MicroAppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MicroApp
        fields = ('id','name','description','type','category','latitude','longitude','startTime','endTime','icon','source')

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id','transactor','amount','time','type')