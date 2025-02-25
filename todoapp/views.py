from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.shortcuts import render, redirect, get_object_or_404  # ✅ Import get_object_or_404


def home(request):
    tasks = Task.objects.all()  
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")  
    else:
        form = TaskForm()
    
    return render(request, "todoapp/home.html", {"tasks": tasks, "form": form}) 


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)  
    task.delete()  
    return redirect("home")  

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)  
    task.completed = True 
    task.save()
    return redirect("home") 

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)  
    task.completed = True  
    task.save()
    return redirect("home")  
