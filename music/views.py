from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Album
from music.forms import AlbumForm


# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'albums': all_albums})

def album_detail(request, pk):
    album = Album.objects.get(pk=pk)
    return render(request, 'music/album_detail.html', {'album': album})


def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AlbumForm()
    return render(request, 'music/create_album.html', {'form': form})

def album_edit(request, pk):
    post = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('album_detail', pk=post.pk)
    else:
        form = AlbumForm(instance=post)
    return render(request, 'music/album_edit.html', {'form': form})

def album_delete(request, pk):
    post = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('home')
    return render(request, 'music/album_delete.html')

class Images(ListView):
    model = Album
    template_name = 'base.html'
