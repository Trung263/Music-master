from django.shortcuts import render,redirect
from appmusic import models
from django.urls import reverse_lazy
import os
import spotipy
from django.conf import settings
from spotipy.oauth2 import SpotifyClientCredentials
from appmusic.forms import CustomCreateSong
from appmusic.models import Song
from django.db.models.signals import pre_delete
from spotipy.exceptions import SpotifyException
from django.dispatch import receiver
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView



# Create your views here.


def searchArtist(request):
    client_credentials_manager = SpotifyClientCredentials(
        client_id=settings.SPOTIPY_CLIENT_ID, 
        client_secret=settings.SPOTIPY_CLIENT_SECRET
    )
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    valueSearch = request.GET.get('search')
    results = {
        'tracks': [],
        'playlists': [],
        'artists': []
    }

    if valueSearch:
        spotify_results = sp.search(q=valueSearch, limit=9, type='track,playlist,artist')
        
        # Get tracks
        if 'tracks' in spotify_results:
            results['tracks'] = spotify_results['tracks']['items']
        
        # Get playlists
        if 'playlists' in spotify_results:
            results['playlists'] = spotify_results['playlists']['items']
        
        # Get artists
        if 'artists' in spotify_results:
            results['artists'] = spotify_results['artists']['items']

    return render(request, 'search_music.html', {'results': results, 'valueSearch': valueSearch})



def index(request):

    client_credentials_manager=SpotifyClientCredentials(client_id=settings.SPOTIPY_CLIENT_ID,client_secret=settings.SPOTIPY_CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    

    first_playlist_id = "0aiBKNSqiPnhtcw1QlXK5s"
    second_playlist_id = "5ttuZoKUA8dgz9MyFeNjxZ"
    top_artists_playlist_id = "6XFOsAdp88ptBCdqUMAfmP"

    

    nameList1 = sp.playlist(first_playlist_id, additional_types=('track',))['name']
    nameList2 = sp.playlist(second_playlist_id, additional_types=('track',))['name']
 
    playlist_tracks_info = sp.playlist_tracks(first_playlist_id,limit=12)
    second_playlist_tracks_info = sp.playlist_tracks(second_playlist_id,limit=12)
    top_artists_tracks_info = sp.playlist_tracks(top_artists_playlist_id, limit=5)

    new_songs = []
    for item in playlist_tracks_info['items']:
        track = item['track']
        new_songs.append({
            'name': track['name'],  # Tên bài hát
            'artists': ', '.join([artist['name'] for artist in track['artists']]),  # Danh sách nghệ sĩ
            'image': track['album']['images'][0]['url'],  # Hình ảnh album (size lớn nhất)
            'preview_url': track['preview_url'],  # URL audio preview
        })

    
    
    second_list = []
    for item in second_playlist_tracks_info['items']:
        track = item['track']
        second_list.append({
            'name': track['name'],  # Tên bài hát
            'artists': ', '.join([artist['name'] for artist in track['artists']]),  # Danh sách nghệ sĩ
            'album': track['album']['name'],  # Tên album
            'added_at': item['added_at'],  # Ngày thêm vào playlist
            'image': track['album']['images'][0]['url'],  # Hình ảnh album (size lớn nhất)
            'preview_url': track['preview_url'],  # URL audio preview
        })

    
    
    artists = []
    for track in top_artists_tracks_info['items']:
        artist = track['track']['artists'][0]
        artist_id = sp.artist(artist['id'])
        artist_info = {
            'name': artist['name'],
            'url': artist['external_urls']['spotify'],
            'image': artist_id['images'][0]['url']
        }
        if artist_info not in artists: 
            artists.append(artist_info)

    context = {
        'new_songs': new_songs,
        'second_list': second_list,
        'name_list1': nameList1,
        'name_list2': nameList2,
        'artists': artists,
        }
    return render(request, 'index.html', context)


class MusicDetailView(DetailView):
    context_object_name = 'music_detail'
    model = models.Song
    template_name = 'music_detail.html'

def MusicCreateView(request):
    if request.method == 'POST':
        form = CustomCreateSong(request.POST,request.FILES)
        if form.is_valid():
            song = form.save()
            if 'image' in request.FILES:
                song.image = request.FILES['image']
                song.save()
            if 'audio_file' in request.FILES:
                song.audio_file = request.FILES['audio_file']
                song.save()
            
            return redirect('appmusic:index')
    else:
        form = CustomCreateSong()

    return render(request, 'create_music.html', {'form': form})

class MusicUpdateView(UpdateView):
    fields = ("title","artist","category","image")
    model = models.Song
    template_name = 'create_music.html'

class MusicDeleteView(DeleteView):
    model = models.Song
    success_url = reverse_lazy("appmusic:index")
    template_name = 'music_confirm_delete.html'
@receiver(pre_delete, sender=models.Song)
def song_pre_delete_handler(sender, instance, **kwargs):
    # Xác định đường dẫn của tệp tin để xóa
    file_image_path = instance.image.path
    file_audio_path = instance.audio_file.path
    
    # Xóa tệp tin nếu tồn tại
    if os.path.isfile(file_image_path):
        os.remove(file_image_path)
    if os.path.isfile(file_audio_path):
        os.remove(file_audio_path)