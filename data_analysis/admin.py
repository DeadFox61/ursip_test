from django.contrib import admin


from .models import Analysis, AnalysisSumByDate
from .constants import DATA_FIELDS


@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):
    list_display = ("date", "company_name", *DATA_FIELDS)


@admin.register(AnalysisSumByDate)
class AnalysisSumByDateAdmin(admin.ModelAdmin):
    list_display = ("date", *DATA_FIELDS)
