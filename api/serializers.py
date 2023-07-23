from rest_framework import serializers
from base.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "first_name",
            "last_name",
            "middle_name",
            "birthday",
            "height",
            "weight",
            "bio",
        ]
