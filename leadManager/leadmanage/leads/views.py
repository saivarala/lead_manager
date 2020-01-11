from django.shortcuts import render

# Create your views here.
from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer


class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permissions =[permissions.AllowAny]
    serializer_class = LeadSerializer