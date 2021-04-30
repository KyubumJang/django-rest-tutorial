from rest_framework import serializers
from files.models import Files, LANGUAGE_CHOICES, STYLE_CHOICES


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']