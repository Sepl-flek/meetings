from rest_framework.serializers import ModelSerializer

from user.models import Profile


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ('information', 'status')
