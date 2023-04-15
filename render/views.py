from django.shortcuts import render

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

    return render(request, 'index.html')


def visitors(request):

    users = Visitor.objects.all()
    return render(request, 'visitors.html', {'names': users})

