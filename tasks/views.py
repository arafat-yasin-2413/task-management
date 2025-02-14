from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import *
from tasks.models import *
from datetime import date
from django.db.models import Q, Count, Max, Min, Avg
# Create your views here.

def manager_dashboard(request):
    return render(request,'dashboard/manager-dashboard.html')

def user_dashboard(request):
    return render(request, 'dashboard/user-dashboard.html')

def test(request):
    names = ["Mahmud", "Ahmed", "John", "Mr. X"]
    count = 0
    
    for name in names:
        count += 1
        
        
    context = {
        "names": names,
        "age" : 23,
        'count':count
    }
    return render(request,'test.html',context)


def create_task(request):
    # employees = Employee.objects.all()
    form = TaskModelForm()
    
    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            """ for Model Form data """
            print(form)
            form.save()
            
            return render(request,'task_form.html',{'form':form, 'message':"Task added successfully"})
            
            
            """ for django form data """
            # print(form.cleaned_data)
            # data = form.cleaned_data
            # title = data.get('title')
            # description = data.get('description')
            # due_date = data.get('due_date')
            # assigned_to = data.get('assigned_to')
            
            # task = Task.objects.create(title=title,description=description, due_date = due_date)
            
            # for emp_id in assigned_to:
            #     employee = Employee.objects.get(id = emp_id)
            #     task.assigned_to.add(employee)
                
            # return HttpResponse("Task Added successfully")
                
            
    
    context = {"form":form}
    return render(request,'task_form.html',context)




def view_task(request):
    # tasks = Task.objects.all()
    # tasks = Task.objects.select_related('details').all()
    # tasks = TaskDetail.objects.select_related('task').all()
    
    # foreign key only (Many to One)
    # tasks = Task.objects.select_related('project').all()
    
    
    """ 
    prefetch related diye Project er maddhome task access korbo 
    reverse foreign key, manay to many te eita kaj kore
    """
    # tasks = Project.objects.prefetch_related('task_set').all()
    # tasks = Task.objects.prefetch_related("assigned_to").all()
    
    
    # task_count = Task.objects.aggregate(num_task = Count('id'))
    projects = Project.objects.annotate(num_task = Count('task')).order_by('num_task')
    return render(request, 'show_task.html', {'projects': projects})
