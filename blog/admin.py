from django.contrib import admin

from blog.models import Article
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article, ArticleAdmin)