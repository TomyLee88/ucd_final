from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import EventForm
from .forms import UserSearchForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Event

def home(request):
    events = Event.objects.all()
    return render(request, 'event_social_network/home.html', {'events': events})

def about(request):
    return render(request, 'event_social_network/about.html')

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user
            event.save()
            return redirect('home')
    else:
        form = EventForm()
    return render(request, 'event_social_network/create_event.html', {'form': form})

def all_events(request):
    events = Event.objects.all()
    return render(request, 'event_social_network/events_list.html', {'events': events})

def user_search(request):
    if request.method == 'GET':
        form = UserSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            # Perform search query
            search_results = User.objects.filter(username__icontains=query)
            return render(request, 'event_social_network/search_results.html', {'search_results': search_results, 'query': query})
    else:
        form = UserSearchForm()
    return render(request, 'event_social_network/user_search.html', {'form': form})

@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, creator=request.user)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EventForm(instance=event)
    return render(request, 'event_social_network/edit_event.html', {'form': form})

@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, creator=request.user)
    if request.method == 'POST':
        event.delete()
        return redirect('home')
    return render(request, 'event_social_network/delete_event.html', {'event': event})