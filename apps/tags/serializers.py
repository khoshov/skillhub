from rest_framework import serializers

from tags.models import Tag, TagMatch


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class TagMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagMatch
        fields = '__all__'
