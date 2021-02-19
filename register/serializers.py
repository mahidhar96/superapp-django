from rest_framework import serializers

from .models import MicroApp

class MicroAppSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MicroApp
        fields = ('id','name','description','type','icon','source')