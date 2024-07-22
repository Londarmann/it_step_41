from django import forms

from .models import Group, Category, Event, Attendee


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', "group"]


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', "category", "date"]


class AttendeeForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = ['name', "event"]

