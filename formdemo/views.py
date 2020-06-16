from django.shortcuts import render
from .models import Formdemo

# Create your views here.
def formdemo_list(request):
    context = {
        'formdemo_list' : Formdemo.objects.all(),
    }
    return render(request, 'formdemo/formdemo_list.html', context)
