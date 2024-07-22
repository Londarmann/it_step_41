from django.contrib import admin

from .models import Group, Category, Event, Attendee


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'group')
    list_filter = ('group',)
    search_fields = ('name',)

class AttendeeInline(admin.TabularInline):
    model = Attendee
    extra = 1

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'date')
    list_filter = ('category', 'date')
    search_fields = ('name',)
    inlines = [AttendeeInline]

@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'event')
    list_filter = ('event',)
    search_fields = ('name',)
