from django.urls import path
from . import views

app_name = 'sendmail'
urlpatterns = [
    path('send-email/', views.index, name='index'),
    path('',views.IndexView.as_view(), name="index"),
]
