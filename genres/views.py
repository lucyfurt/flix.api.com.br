from rest_framework import generics
from genres.models import Genre
from genres.serializers import GenreSerializer
from rest_framework.permissions import IsAuthenticated
    
    
class GenreListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )   
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer 
    
