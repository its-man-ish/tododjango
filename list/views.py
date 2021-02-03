from django.shortcuts import render, HttpResponseRedirect
from .models import TodoModel
from .forms import TodoForm
# Create your views here.
def index(request):
    reg =0
    fm =0
    if request.method =='POST':
        fm = TodoForm(request.POST)
        if fm.is_valid():
            em=fm.cleaned_data['email']
            nm=fm.cleaned_data['name']
            wk=fm.cleaned_data['work']
            tm=fm.cleaned_data['time']
            reg = TodoModel(email=em,name=nm,work=wk,time=tm)
            reg.save()
            fm=TodoForm()
    reg=TodoModel.objects.all()
    return render(request,'list/index.html',{
        'form':fm,
        'todo':reg,
          })


def delete_work(request,id):
    if request.method =='POST':
        pi = TodoModel.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')