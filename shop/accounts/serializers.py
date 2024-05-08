from rest_framework import serializers

from .models import CustomUser



class ProfileSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField(source='get_avatar')
    class Meta:
        model = CustomUser
        fields = ('avatar', 'email', 'phone', 'fullName')

    def get_avatar(self, obj):
        if obj.src:
            return {'src': obj.src.url, 'alt': obj.alt}
        return None