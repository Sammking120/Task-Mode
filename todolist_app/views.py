'''view'''
from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from todolist_app.models import Tasklist
from todolist_app.forms import Taskform



def todolist(request):
    ''' Send Data to Database'''
    if request.method == "POST":
        form = Taskform(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ("A New Message Has been Added Successfully"))
        return redirect('todolist')
    else:
        all_tasks = Tasklist.objects.all()
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks': all_tasks})

def delete_task(request, task_id):
    '''Delete Task'''
    task = Tasklist.objects.get(pk=task_id)
    task.delete()

    return redirect('todolist')


def edit_task(request, task_id):
    '''Update on Database'''
    if request.method == "POST":
        taske = Tasklist.objects.get(pk=task_id)
        form = Taskform(request.POST or None, instance=taske)
        if form.is_valid():
            form.save()

        messages.success(request, ("Task Edited"))
        return redirect('todolist')
    else:
        task_obj = Tasklist.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})

def complete_task(request, task_id):
    '''Complete Task'''
    task = Tasklist.objects.get(pk=task_id)
    task.done = True
    task.save()

    return redirect('todolist')


def pending_task(request, task_id):
    '''Complete Task'''
    task = Tasklist.objects.get(pk=task_id)
    task.done = False
    task.save()

    return redirect('todolist')


def about(request):
    '''about Page'''
    context = {

        'About_Text':" Welcome to the About Us Page"
        }
    return render(request, 'about-us.html', context)

def contact(request):
    '''Contact Us'''
    context = {
        'Contact_Text':"Welcome to the Contact Us Page"
        }

    return render(request, 'contact.html', context)


def index(request):
    '''Home page'''
    context = {
        'index_Text':"Welcome to the Home Page"
        }

    return render(request, 'index.html', context)
