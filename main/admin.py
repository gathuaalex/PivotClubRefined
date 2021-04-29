from django.contrib import admin

from main.models import Project, ResearchPaper, Team, Gallery

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)


class ResearchPaperAdmin(admin.ModelAdmin):
    pass

admin.site.register(ResearchPaper, ResearchPaperAdmin)


class TeamAdmin(admin.ModelAdmin):
    pass

admin.site.register(Team, TeamAdmin)


class GalleryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Gallery, GalleryAdmin)