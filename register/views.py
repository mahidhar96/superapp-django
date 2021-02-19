from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import MicroAppSerializer
from .models import MicroApp


class MicroAppViewSet(viewsets.ModelViewSet):
    queryset = MicroApp.objects.all().order_by('id')
    serializer_class = MicroAppSerializer