from django.shortcuts import render,redirect

from django.http  import HttpResponse,Http404,HttpResponseRedirect
import datetime as dt
from django.contrib.auth.decorators import login_required

# @login_required(login_url='/accounts/login/')
def admin(request):
    return render(request)
