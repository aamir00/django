from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_POST

# Create your views here.

def index(request):
    todo_all_res = Todo.objects.order_by('id')
    todo_form = TodoForm()
    # to get all records
    context={'todo_all_res' : todo_all_res, 'form' : todo_form }
    #context can be passed to the template and can be used their
    return render(request, 'todo/index.html', context)

@require_POST
def addTodo(request):
    todo_form = TodoForm(request.POST)
    if todo_form.is_valid():
        todo = Todo(text = request.POST['todo_text'])
        todo.save()
    return redirect('index')

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete=True
    todo.save()
    print("deleted ", todo_id)
    return redirect('index')

def deleteCompleted(request):
    todo = Todo.objects.filter(complete__exact=True)
    print("Inside del complete", todo)
    todo.delete()
    return redirect('index')

def deleteAll(request):
    todo = Todo.objects.filter();
    todo.delete()
    return redirect('index')
