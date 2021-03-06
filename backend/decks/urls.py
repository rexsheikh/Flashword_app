from django.urls import path, include
from . import views

# <<<<<<<<<<<<<<<<< EXAMPLE FOR STARTER CODE USE <<<<<<<<<<<<<<<<<

urlpatterns = [
    path('', views.user_decks),
    path('update_word_score/<str:word_search>/<int:score>/',
         views.update_word_score),
    path('get_word/<str:word_search>/', views.get_word),
    path('add_word/<str:title_search>/<str:word>/', views.add_word),
    path('word_list/', views.word_list),
    path('get_deck/<int:pk>/', views.get_deck),
    path('date_list/', views.date_list),
    path('update_word_reviews/<str:word_search>/<str:date_search>/',
         views.update_word_reviews),
    path('review_average/', views.review_average),
    path('delete_deck/<str:deck_title>/', views.delete_deck),
    path('delete_word/<str:word_search>/', views.delete_word),
]
