from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.utils.safestring import mark_safe
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Supplier

def index(request):
    context={
    }
    return render(request,'chat/index.html',context)
@login_required
def room(request,room_name):

    context={
    'room_name':room_name,
    'username':mark_safe(json.dumps(request.user.username))
    }
    return render(request,'chat/room.html',context)
