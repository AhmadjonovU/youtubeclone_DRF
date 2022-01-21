from django.shortcuts import render
from .models import *
from rest_framework import generics
from .serializers import PlaylistSerilizer,CommentSerilizer,VideoSerilizer
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework.permissions import IsAuthenticated



class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serilizer_class = PlaylistSerilizer

class PlaylistList(generics.ListAPIView):
    queryset = Playlist.objects.all()
    serilizer_class = PlaylistSerilizer
    permission_class = [IsAuthenticated, ] 
    filter_backends = [SearchFilter,]
    search_fields = ["title"]

class anPlaylist(generics.RetrieveAPIView): 
    queryset = Playlist.objects.all() 
    serializer_class = PlaylistSerilizer
    permission_class = [IsAuthenticated, ] 

class CreatePlaylist(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerilizer
    permission_class = [IsAuthenticated, ] 

class DelatePlaylist(generics.RetrieveDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerilizer
    permission_class = [IsAuthenticated, ] 


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serilizer_class = CommentSerilizer
    permission_class = [IsAuthenticated, ] 

class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serilizer_class = CommentSerilizer
    permission_class = [IsAuthenticated, ] 
    filter_backends = [SearchFilter,]
    search_fields = ["matn"]

class anComment(generics.RetrieveAPIView): 
    queryset = Comment.objects.all() 
    serializer_class = CommentSerilizer
    permission_class = [IsAuthenticated, ] 

class CreateComment(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerilizer
    permission_class = [IsAuthenticated, ] 

class DelateComment(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerilizer
    permission_class = [IsAuthenticated, ] 


class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serilizer_class = VideoSerilizer
    permission_class = [IsAuthenticated, ] 

class VideoList(generics.ListAPIView):
    queryset = Video.objects.all()
    serilizer_class = VideoSerilizer
    permission_class = [IsAuthenticated, ] 
    filter_backends = [SearchFilter,]
    search_fields = ["title"]

class anVideo(generics.RetrieveAPIView): 
    queryset = Video.objects.all() 
    serializer_class = VideoSerilizer
    permission_class = [IsAuthenticated, ] 

class CreateVideo(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerilizer
    permission_class = [IsAuthenticated, ] 

class DelateVideo(generics.RetrieveDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerilizer
    permission_class = [IsAuthenticated, ] 




