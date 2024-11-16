from django.shortcuts import redirect
from .forms import ObituaryForm
from django.shortcuts import render


def obituary_submit(request):
    if request.method == 'POST':
        form = ObituaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('obituary_submit')
    else:
        form = ObituaryForm()
    return render(request, 'obituaries/obituary_submit.html', {'form': form})
from django.shortcuts import render

def obituary_list(request):
    
    obituaries = [
        {"name": "John Doe", "date": "2024-11-12", "message": "Loving husband and father."},
        {"name": "Jane Smith", "date": "2024-11-10", "message": "A kind soul, forever in our hearts."}
    ]
    return render(request, 'obituaries/obituary_list.html', {'obituaries': obituaries})

def obituary_submit(request):
    return render(request, 'obituaries/obituary_submit.html')

from django.shortcuts import render

def obituary_detail(request, obituary_id):
    obituary = {
        "id": obituary_id,
        "name": "John Doe",
        "date": "2024-11-12",
        "message": "Loving husband and father. Forever in our hearts."
    }
    return render(request, 'obituaries/obituary_detail.html', {'obituary': obituary})

def obituary_submit(request):
    return render(request, 'obituaries/obituary_submit.html')
