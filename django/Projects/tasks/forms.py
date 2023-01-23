from django import forms

class TaskForm(forms.Form):
    task_name = forms.CharField(max_length=100)
    task_description = forms.CharField(max_length=500, required=False)
    task_due_date = forms.DateField(required=False)
