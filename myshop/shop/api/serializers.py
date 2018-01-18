from rest_framework import serializers
from shop.models import Category


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')
