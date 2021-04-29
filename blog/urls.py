from django.urls import path

from blog import views

urlpatterns = [
    path("", views.ArticleListView.as_view(), name="blog"),
    path("<int:pk>", views.ArticleDetailView.as_view(), name="article-detail")
]