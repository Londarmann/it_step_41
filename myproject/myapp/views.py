from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import GroupForm, CategoryForm, EventForm, AttendeeForm
from .models import Group, Category, Event, Attendee


class GroupListView(ListView):
    model = Group
    template_name = "myapp/group_list.html"
    context_object_name = "groups"


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = "myapp/group_form.html"
    success_url = reverse_lazy("group-list")


class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm
    template_name = "myapp/group_form.html"
    success_url = reverse_lazy("group-list")


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'myapp/group_confirm_delete.html'
    success_url = reverse_lazy('group-list')


class CategoryListView(ListView):
    model = Category
    template_name = "myapp/category_list.html"
    context_object_name = "categories"


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "myapp/category_form.html"
    success_url = reverse_lazy("category-list")


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "myapp/category_form.html"
    success_url = reverse_lazy("category-list")


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'myapp/category_confirm_delete.html'
    success_url = reverse_lazy('category-list')


class EventListView(ListView):
    model = Event
    form_class = EventForm
    template_name = "myapp/event_list.html"
    context_object_name = "events"


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = "myapp/event_form.html"
    success_url = reverse_lazy("event-list")


class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = "myapp/event_form.html"
    success_url = reverse_lazy("event-list")


class EventDeleteView(DeleteView):
    model = Event
    template_name = 'myapp/event_confirm_delete.html'
    success_url = reverse_lazy('event-list')


class AttendeeListView(ListView):
    model = Attendee
    template_name = "myapp/attendee_list.html"
    context_object_name = "attendees"


class AttendeeCreateView(CreateView):
    model = Attendee
    form_class = AttendeeForm
    template_name = "myapp/attendee_form.html"
    success_url = reverse_lazy("attendee-list")


class AttendeeUpdateView(UpdateView):
    model = Attendee
    form_class = AttendeeForm
    template_name = "myapp/attendee_form.html"
    success_url = reverse_lazy("attendee-list")


class AttendeeDeleteView(DeleteView):
    model = Attendee
    template_name = "myapp/attendee_confirm_delete.html"
    success_url = reverse_lazy("attendee-list")


class RegisterView(View):
    form_class = UserCreationForm
    template_name = "myapp/register.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('group-list')
        return render(request, self.template_name, {'form': form})


class CustomLoginView(LoginView):
    template_name = "myapp/login.html"


class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('group-list')


