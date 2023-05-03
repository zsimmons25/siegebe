from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SiegeSerializer
from .models import Siege

class SiegeView(viewsets.ModelViewSet):
    serializer_class = SiegeSerializer
    queryset = Siege.objects.all()