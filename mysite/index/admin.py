from django.contrib import admin

from .models import GeneralSkillsAnalytics, FiltredSkillsAnalytics, GeneralAnalytics, FiltredAnalytics

admin.site.register(GeneralSkillsAnalytics)
admin.site.register(FiltredSkillsAnalytics)
admin.site.register(GeneralAnalytics)
admin.site.register(FiltredAnalytics)
