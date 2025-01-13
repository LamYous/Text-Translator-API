from django.urls import path
from . import views

urlpatterns = [
    path('', views.TranslateTextView.as_view(), name="translate_text"),
]