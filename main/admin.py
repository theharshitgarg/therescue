from django.contrib import admin

# Register your models here.
from .models import *

# admin.site.register(Rescuer)
admin.site.register(Animal)

class RescuerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['first_name', 'last_name', 'user_id']}),
    ]

    list_display = ('first_name', 'last_name', 'user_id')
    list_filter = ['first_name', 'user_id']
    search_fields = ['first_name', 'last_name', 'user_id']

class RescueOperationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['rescue_id']}),
    ]
    list_display = ( 'rescue_id',)
    list_filter = ['started_by', 'started_on', 'closed_on']
    search_fields = ['started_by', 'rescue_id', 'started_on', 'closed_on']

admin.site.register(Rescuer, RescuerAdmin)
admin.site.register(RescueOperation, RescueOperationAdmin)
