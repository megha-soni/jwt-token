from rest_framework import serializers
from .models import User
class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['email','password','is_varified']

class Loginserializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField()


class Accountverifyserializer(serializers.Serializer):
    email=serializers.EmailField()    
    otp=serializers.CharField()