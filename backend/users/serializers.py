from .models import Profile, Team
from rest_framework import serializers


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('name', 'description', 'created_by')
