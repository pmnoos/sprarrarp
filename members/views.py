from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from .models import Individual, Member, EventInfo
from . forms import MemberForm
from django.contrib import messages
from datetime import datetime

# Create your views here.

def MemberFormView(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.save()
            messages.success(request, 'Member successfully added!')
            return HttpResponseRedirect('/members/')
    else:
        form = MemberForm()
    return render(request, 'members/member_form.html', {'form': form})

