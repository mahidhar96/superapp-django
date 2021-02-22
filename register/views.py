from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import MicroAppSerializer,TransactionSerializer
from .models import MicroApp,Transaction


class MicroAppViewSet(viewsets.ModelViewSet):
    queryset = MicroApp.objects.all().order_by('id')
    serializer_class = MicroAppSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all().order_by('id').reverse()
    serializer_class = TransactionSerializer