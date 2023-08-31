from django.shortcuts import render

def task_view(request):
    dynamic_data = "Hello, this is dynamic data!"
    return render(request, 'myapp/task.html', {'dynamic_data': dynamic_data})
