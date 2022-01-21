
from django.shortcuts import render
from .models import *
from rest_framework import generics
from .serializers import KanalSerilizer,UserSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework.permissions import IsAuthenticated


class KanalViewSet(ModelViewSet):
    queryset = Kanal.objects.all()
    serilizer_class = KanalSerilizer
    permission_class = [IsAuthenticated, ] 

class KanalList(generics.ListAPIView):
    queryset = Kanal.objects.all()
    serilizer_class = KanalSerilizer
    permission_class = [IsAuthenticated, ] 
    filter_backends = [SearchFilter,]
    search_fields = ["user"]

class anKanal(generics.RetrieveAPIView): 
    queryset = Kanal.objects.all() 
    serializer_class = KanalSerilizer
    permission_class = [IsAuthenticated, ] 

class CreateKanal(generics.ListCreateAPIView):
    queryset = Kanal.objects.all()
    serializer_class = KanalSerilizer
    permission_class = [IsAuthenticated, ] 

class DelateKanal(generics.RetrieveDestroyAPIView):
    queryset = Kanal.objects.all()
    serializer_class = KanalSerilizer
    permission_class = [IsAuthenticated, ]


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serilizer_class = UserSerializer
    permission_class = [IsAuthenticated, ] 

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serilizer_class = KanalSerilizer
    permission_class = [IsAuthenticated, ] 
    filter_backends = [SearchFilter,]
    search_fields = ["user"] 

class CreateUser(generics.ListAPIView):
    queryset = User.objects.all()
    serilizer_class = KanalSerilizer
    permission_class = [IsAuthenticated, ] 


