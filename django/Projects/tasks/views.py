from django.shortcuts import redirect, render
from .forms import TaskForm

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # process the form data
            return redirect('tasks')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})
