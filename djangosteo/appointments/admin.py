from django.contrib import admin

from . import models
class AppointmentAdmin(admin.ModelAdmin):
    search_fields = ['practitioner', 'specialization']
    list_filter = ['practitioner']
    # list_display = ['title', 'created_at', 'is_live', 'time_to_complete', 'status']
    # list_editable = ['status',]
    # actions = [make_published, make_reviewed, make_in_progress]




# class YearListFilter(admin.SimpleListFilter):
#     title = 'Year created'
#     parameter_name = 'year'
#
#     def lookups(self, request, model_admin):
#         return (
#             ('2015', '2015'),
#             ('2016', '2016'),
#         )
#
#     def queryset(self, request, queryset):
#         if self.value() == '2015':
#             return queryset.filter(created_at__gte=date(2015, 1, 1),
#                                    created_at__lte=date(2015, 12, 31))
#
#         if self.value() == '2016':
#             return queryset.filter(created_at__gte=date(2016, 1, 1),
#                                    created_at__lte=date(2016, 12, 31))
admin.site.register(models.Appointment, AppointmentAdmin)
admin.site.register(models.Practitioner)
admin.site.register(models.Specialization)
admin.site.register(models.Patient)
