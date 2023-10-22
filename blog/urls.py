from django.urls import path
from .views import BlogListView
app_name="blog"

urlpatterns = [
    #path('', views.index, name='index'),
    path('', BlogListView.as_view(), name="home")
]