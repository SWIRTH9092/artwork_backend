from .models import Artwork
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our ArtSerializer
class ArtworkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Artwork
        # the fields that should be included in the serialized output
        fields = ['id', 'subject', 'category', 'comments', 'image_url']
        
