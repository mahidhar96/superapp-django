from rest_framework import serializers

from .models import MicroApp,Transaction,BookingItem

class MicroAppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MicroApp
        fields = ('id','name','description','type','category','latitude','longitude','startTime','endTime','icon','source')

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id','transactor','amount','time','type')

class BookingItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookingItem
        fields = ('id','name','image','type','rating','additional')