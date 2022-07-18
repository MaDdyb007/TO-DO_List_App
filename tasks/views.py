from django.shortcuts import render, HttpResponseRedirect
from .forms import Taskrecord
from .models import Task

# Create your views here.

#this function for add new task and show all tasks
def add_show(request):
    if request.method == 'POST':
        fm = Taskrecord(request.POST)
        if fm.is_valid():
            tl = fm.cleaned_data['title']
            ds = fm.cleaned_data['description']
            reg = Task(title=tl, description=ds)
            reg.save()
            fm = Taskrecord()
    else:
        fm = Taskrecord()
    tsk = Task.objects.all()

    return render(request,'tasks/addandshow.html',{'form':fm, 'taskd': tsk})


# this function is for update task
def update(request,id):
    if request.method == 'POST':
        tsk = Task.objects.get(pk=id)
        fm = Taskrecord(request.POST, instance=tsk)
        if fm.is_valid():
            fm.save()
    else:
        tsk = Task.objects.get(pk=id)
        fm = Taskrecord(instance=tsk)
    return render(request,'tasks/updatetask.html',{'form':fm})

 #this function will delete the task
def delete(request, id):
    if request.method == 'POST':
        tsk = Task.objects.get(pk=id)
        tsk.delete()
        return HttpResponseRedirect('/')


def complete(request,id):
      if request.method == 'POST':
        tsk = Task.objects.filter(pk=id)
        tsk.update(complete=True)
        print(tsk)
        return HttpResponseRedirect('/')