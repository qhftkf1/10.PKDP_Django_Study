from django.shortcuts import render
from pkdp.models import Member
# Create your views here.

def index(request):
    member = Member.objects.all()

    context = {
        'member' : member,
    }

    return render(request, 'index.html', context = context)
