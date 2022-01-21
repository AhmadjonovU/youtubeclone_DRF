from rest_framework.serializers import ModelSerializer
from .models import Kanal
from django.contrib.auth.models import User

class KanalSerilizer(ModelSerializer):
    class Meta:
        model = Kanal
        fields = "__all__"

class UserSerializer:  
    class Meta:  
        model = User  
        fields = "__all__"  
