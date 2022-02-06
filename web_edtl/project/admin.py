from django.contrib import admin
from project.models import Project, ProjectCategory,\
        Year, ProjectStatus, Fund,\
        ProjectLocation, ProjectBudget, TypeOfProcurament

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectCategory)
admin.site.register(Year)
admin.site.register(ProjectStatus)
admin.site.register(Fund)
admin.site.register(ProjectLocation)
admin.site.register(ProjectBudget)
admin.site.register(TypeOfProcurament)