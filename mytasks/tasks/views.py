from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Task
from .forms import TaskForm, RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'tasks/register.html', {'form': form})

@login_required
def index_view(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/index.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})
