from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Songs
from .serializers import Serializer
# Create your views here.


@api_view(['GET','POST'])
def song_list(request):

    if request.method == 'GET':
        songs = Songs.objects.all()
        serializer = Serializer(songs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

@api_view(['GET','PUT', 'DELETE'])
def song_detail(request,pk):
    song = get_object_or_404(Songs, pk=pk)
    if request.method == 'GET':   
        serializer = Serializer(song);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = Serializer(song, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        song.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

