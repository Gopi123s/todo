from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from  .models import todo,l

# for i in todo:
print(l)
l2=[i[0] for i in l]
print(l2)

# Create your views here.
def home(request):
    todocat=todo.objects.all()
    l2=[i[0] for i in l]
    cat=l2
    


    todo1=todocat
    return render (request,'home.html',{'todo1':todo1,'cat':cat})


def addtask(request):
    if request.method=='POST':
        desc=request.POST['desc']
        date=request.POST['date']
        category=request.POST['category']


def updatemark(request,pk):
    todocat=todo.objects.get(pk=pk)

    if todocat.markcompleted==True:
        todocat.markcompleted=False
    else:
        todocat.markcompleted=True
    todocat.save()

    
    return redirect('home')

def delete(request,pk):
    todocat=todo.objects.get(pk=pk).delete()
    messages.success(request,"data deleted is successfully")
    return redirect('home')


def addtask(request):
    todocat=todo.objects.all()
    if request.method=='POST':
        desc=request.POST['desc']
        date=request.POST.get('date')
        cat=request.POST.get('cat')
        if cat:
            todonew=todo(desc=desc,date=date,category=cat)
        else:
            todonew=todo(desc=desc,date=date)
        
        todonew.save()
       
        return redirect('home')
    return render('home',{'todocat':todo})


def update(request,pk):
    todos=todo.objects.get(id=pk)
    l2=[i[0] for i in l]
    cat=l2
    if request.method=='POST':
        todos.desc=request.POST['desc']
        todos.date=request.POST.get('date')
        todos.category=request.POST.get('cat')
        todos.save()
        return redirect('home')
    

    return render(request,'update.html',{'todos':todos,'cat':cat})