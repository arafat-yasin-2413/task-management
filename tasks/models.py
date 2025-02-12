from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    # eikhane task er ekta reverse relaiton pabo
    

""" 
Project class ta jodi Task class er niche thakto , 
tahole, project = models.ForeignKey(Project, on_delete=models.CASCADE) ... ei line a Project undefined dekhaito.

amra jodi Project class ta nichei rakhte chai tokhon oi line "Project" likhe dite pari. tahole ar not defined dekhabe na. 


but Best practice hocche Project class ta ke upore likha.


"""


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    # parent er moddhe toiri hoy
    # task_set

class Task(models.Model):
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                default=1)
    
    assigned_to = models.ManyToManyField(Employee,related_name='tasks')
    title = models.CharField(max_length=250)
    description = models.TextField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # 1 to 1 er khetre model er naam diyei reverse access kora jay
    # foreign key thakle (Many to 1) model er naam underscore set 
    # diye access korte hoy
    
    
class TaskDetail(models.Model):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'
    
    PRIORITY_OPTIONS = (
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low')
    )
    
    task = models.OneToOneField(Task,
                                on_delete=models.CASCADE,
                                related_name="details")
    assigned_to = models.CharField(max_length=100)
    priority = models.CharField(max_length= 1, choices=PRIORITY_OPTIONS, default=LOW)
    
    
    
    
    
# task = onekgula employee ekta task
# employee = onekgula task ekta employee
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     
    
""" 
In [5]: Project.objects.create(name="Dummy Project",start_date="2025-02-12")
Out[5]: <Project: Project object (1)>

In [6]: project = Project.objects.all()

In [7]: project
Out[7]: <QuerySet [<Project: Project object (1)>]>

In [8]: project.first
Out[8]: <bound method QuerySet.first of <QuerySet [<Project: Project object (1)>]>>

In [9]: project.first()
Out[9]: <Project: Project object (1)>

In [10]: project.first().id
Out[10]: 1


"""
