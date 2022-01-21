from statistics import mode
from rest_framework.serializers import ModelSerializer
from .models import Playlist,Comment,Video

class PlaylistSerilizer(ModelSerializer):
    class Meta:
        model = Playlist
        fields = "__all__"

class CommentSerilizer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class VideoSerilizer(ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"