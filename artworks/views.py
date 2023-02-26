from .models import Artwork
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ArtworkSerializer

class ArtworkViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Artwork.objects.all()
    # The serializer class for serializing output
    serializer_class = ArtworkSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]