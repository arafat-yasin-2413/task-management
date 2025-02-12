from django import forms 
from tasks.models import *


# Django Form
class TaskForm(forms.Form):
    title = forms.CharField(max_length=250, label="Task Title")
    description = forms.CharField(widget=forms.Textarea, label="Task Description")
    due_date = forms.DateField(widget=forms.SelectDateWidget, label="Due Date")
    
    assigned_to = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=[], label="Assigned To")
    
    def __init__(self, *args, **kwargs):
        # print(args, kwargs)
        employees = kwargs.pop("employees", [])
        super().__init__(*args, **kwargs)
        # print(self.fields)
        self.fields['assigned_to'].choices = [
            (emp.id, emp.name) for emp in employees
        ]
        
    
# Mixin for style

class StyledFromMixin:
    # Mixin to apply style to form fields
    default_classes = "border-2 border-gray-300 w-full p-3 rounded-md shadow-md "
    
    def apply_sytle_widgets(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class': self.default_classes,
                    'placeholder': f"Enter {field.label.lower()}"
                }) ,
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': f"{self.default_classes} resize-none",
                    'placeholder': f"Enter {field.label.lower()}",
                    'rows':5
                })
            elif isinstance(field.widget, forms.SelectDateWidget):
                print("Inside date")
                field.widget.attrs.update({
                    'class':"border-2 border-gray-300 p-3 rounded-md shadow-md"
                })
            elif isinstance(field.widget, forms.CheckboxSelectMultiple):
                print("Inside checkbox")
                field.widget.attrs.update({
                    'class': "space-y-2",
                    # 'class':self.default_classes
                })   
            else:
                print("Inside else")
                field.widget.attrs.update({
                    'class': self.default_classes
                })             
    
    
    
# Django Model Form
class TaskModelForm(StyledFromMixin,forms.ModelForm):
    class Meta:
        model = Task
        # fields = '__all__'
        fields = ['title','description','due_date','assigned_to']
        widgets = {
            'due_date': forms.SelectDateWidget,
            'assigned_to': forms.CheckboxSelectMultiple
        }
        
        
        # exclude = ['project', 'is_completed', 'created_at', 'updated_at']
        
        # widgets = {
        #     'title': forms.TextInput(attrs={
        #         'class':"border-2 border-gray-300 rounded-md shadow-md w-full",
        #         'placeholder':"Enter Task Title"
        #     }),
            
        #     'description':forms.Textarea(attrs={
        #         'class':"border-2 border-gray-300 rounded-md shadow-md w-full",
        #         'placeholder':"Provide detailed task description"
        #     }),
            
            
        #     'due_date':forms.SelectDateWidget(attrs={
        #         'class':"border-2 border-gray-300 rounded-md shadow-md w-1/2",
                
        #         }),
        #     'assigned_to':forms.CheckboxSelectMultiple(attrs={
                
        #         'class':"border-2 border-gray-300 rounded-md shadow-md w-full",
                
        #     })
        # }
        
    # widget using Mixins
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_sytle_widgets()
        