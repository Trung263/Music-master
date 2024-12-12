from django.urls import path
from appmusic import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.MusicDetailView.as_view(), name='detail'),
    path('create/', views.MusicCreateView, name='create'),
    path('update/<int:pk>/',views.MusicUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.MusicDeleteView.as_view(),name='delete'),
    # Các URL khác
    path('search', views.searchArtist, name='search_artist'),



]