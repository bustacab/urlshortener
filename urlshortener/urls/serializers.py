from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import URLField

from .models import URL


class URLSerializer(ModelSerializer):
    url = URLField(required=True)

    class Meta:
        fields = ["url"]
        model = URL
