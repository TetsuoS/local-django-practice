from django.shortcuts import render
from .models import Formdemo
from .forms import FormdemoCreateForm

# Create your views here.
def formdemo_list(request):
    context = {
        'formdemo_list' : FormdemoCreateForm()
    }
    return render(request, 'formdemo/formdemo_list.html', context)
