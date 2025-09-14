from django.shortcuts import render, redirect
from .forms import PersonForm

def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PersonForm()
    return render(request, 'myapp/form.html', {'form': form})

def success(request):
    return render(request, 'myapp/success.html')
