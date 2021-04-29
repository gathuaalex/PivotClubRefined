from django.urls import path

from main import views
from blog.views import ArticleListView

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('about', views.AboutView.as_view(), name='about'),
    path('projects', views.ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    path('papers', views.PaperListView.as_view(), name='papers'),
    path('contact', views.contact, name='contact'),
    path('teams', views.TeamListView.as_view(), name='teams'),
    path('gallery', views.GalleryListView.as_view(), name='gallery'),
    path('articles', ArticleListView.as_view(), name='articles'),
]