from django.contrib import admin
from .models import AR_US_STATUS,AR_US_TYPE,AR_USER_STORY
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class AR_US_STATUSAdmin(ImportExportModelAdmin):
    search_fields = ['status_key']
    list_display = ('status_key','status_desc','status_shortcode')


class AR_US_TYPEAdmin(ImportExportModelAdmin):
    search_fields = ['type_key']
    list_display = ('type_key','type_desc','type_short_code')


class AR_USER_STORYAdmin(ImportExportModelAdmin):
    search_fields = ['title']
    list_display = ('title','owner','story_tri_part_text','acceptance_criteria','ac_readability_score','conversation','convo_readability_score','autoscoring_on','archive_indicator','readiness_quality_score','created_by','updated_by','ORG_id')


admin.site.register(AR_US_STATUS,AR_US_STATUSAdmin)
admin.site.register(AR_US_TYPE,AR_US_TYPEAdmin)
admin.site.register(AR_USER_STORY,AR_USER_STORYAdmin)
