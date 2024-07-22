from django.contrib import admin

from django.urls import path

from .views import GroupListView, GroupUpdateView, GroupCreateView, GroupDeleteView, CategoryListView, \
    CategoryCreateView, CategoryUpdateView, CategoryDeleteView, EventListView, EventCreateView, EventUpdateView, \
    EventDeleteView, AttendeeListView, AttendeeDeleteView, AttendeeCreateView, AttendeeUpdateView, RegisterView, \
    CustomLoginView, CustomLogoutView

urlpatterns = [
    path('accounts/profile/',  GroupListView.as_view(), name='group-list'),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path('groups/', GroupListView.as_view(), name='group-list'),
    path('groups/add/', GroupCreateView.as_view(), name='group-add'),
    path('groups/<int:pk>/edit/', GroupUpdateView.as_view(), name='group-edit'),
    path('groups/<int:pk>/delete/', GroupDeleteView.as_view(), name='group-delete'),

    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/add/', CategoryCreateView.as_view(), name='category-add'),
    path('categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category-edit'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),

    path('events/', EventListView.as_view(), name='event-list'),
    path('events/add/', EventCreateView.as_view(), name='event-add'),
    path('events/<int:pk>/edit/', EventUpdateView.as_view(), name='event-edit'),
    path('events/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),

    path('attendees/', AttendeeListView.as_view(), name='attendee-list'),
    path('attendees/add/', AttendeeCreateView.as_view(), name='attendee-add'),
    path('attendees/<int:pk>/edit/', AttendeeUpdateView.as_view(), name='attendee-edit'),
    path('attendees/<int:pk>/delete/', AttendeeDeleteView.as_view(), name='attendee-delete'),
]
