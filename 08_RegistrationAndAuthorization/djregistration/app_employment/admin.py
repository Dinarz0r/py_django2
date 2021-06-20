from django.contrib import admin
from .models import Vacancy, Summary


class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class SummaryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'create_at']


admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Summary, SummaryAdmin)


