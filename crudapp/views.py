from django.shortcuts import render
from .forms import StudentForm

def insert_view(request):
    form= StudentForm(request.GET)
    if form.is_valid():
        form.save()
    return render(request, 'star/index.html', {'form': form })
