from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Album, Favorite, User
from music.forms import AlbumForm


# Create your views here.
def index(request):
    all_albums = Album.objects.all().order_by('title')
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

def add_favorite(request, res_pk):
    album = get_object_or_404(Album, pk=res_pk)
    unfavorited = False
    for favorite in request.user.favorites.all():
        if album == favorite.album:
            favorite.delete()
            unfavorited = True
    if not unfavorited:
        favorite = Favorite.objects.create(album=album, user=request.user)
        favorite.save()
    return redirect("home")

def favorite(request):
    favorited = Favorite.objects.all().order_by('-created_at')
    return render(request, 'music/favorites.html', {'favorited': favorited})