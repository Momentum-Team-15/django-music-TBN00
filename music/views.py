from django.shortcuts import render
from .models import Album


# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'albums': all_albums})

def album_detail(request, pk):
    album = Album.objects.get(pk=pk)
    return render(request, 'music/album_detail.html', {'album': album})