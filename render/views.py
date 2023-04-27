from django.shortcuts import render
from django.contrib import messages

from .models import Visitor
from .helper import is_profane


# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        print(name)
        if not is_profane(name):
            visitor = Visitor(name=name)
            visitor.save()
            messages.success(request, "Your input has been successfully added.")
        else:
            messages.success(request, "You have entered a profane word and it cannot be submitted.")
    return render(request, 'index.html')


def visitors(request):

    users = Visitor.objects.all()
    return render(request, 'visitors.html', {'names': users})