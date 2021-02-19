from django.shortcuts import render
from .forms import StudentForm
from .models import Student

def insert_view(request):
    form= StudentForm(request.GET)
    if form.is_valid():
        form.save()
    return render(request, 'star/index.html', {'form': form })

def display(request):
	st=Student.objects.all() # Collect all records from table
	return render(request,'display.html',{'st':st})    
