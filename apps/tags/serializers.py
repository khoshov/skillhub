from rest_framework import serializers

from tags.models import Tag, TagMatch, TagOption


class TagOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagOption
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    options = TagOptionSerializer(many=True)

    class Meta:
        model = Tag
        fields = '__all__'


class TagMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagMatch
        fields = '__all__'
