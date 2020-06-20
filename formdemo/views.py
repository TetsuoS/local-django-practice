from django.shortcuts import render, redirect, get_object_or_404
from .models import Formdemo
from .forms import FormdemoCreateForm

# Create your views here.
def formdemo_create(request):

    form = FormdemoCreateForm(request.POST or None)
    if request.method == 'GET':

        context = {
            'formdemo_create' : FormdemoCreateForm()
        }
        return render(request, 'formdemo/formdemo_create.html', context)

    else:

        form.save()
        return redirect('/formdemo')

def formdemo_top(request):
    return render(request, 'formdemo/formdemo_top.html')

def formdemo_detail(request, pk):

    details = Formdemo.objects.get(pk=pk)
    context = {
        'details' : details,
    }
    return render(request, 'formdemo/formdemo_detail.html', context)

def formdemo_update(request):
    return render(request, 'formdemo/formdemo_update.html')
    
"""
def formdemo_update(request, pk):
    messages = get_object_or_404(Formdemo, pk=pk)
    form = FormdemoCreateForm(request.POST or None, instance=messages)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/formdemo')

    context = {
        'form' : form
    }
    return render(request, 'formdemo/formdemo_update.html', context)
"""
def formdemo_delete(request):
    return render(request, 'formdemo/formdemo_delete.html')