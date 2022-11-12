from django.contrib import messages
from django.shortcuts import render, redirect
from digits.forms import UploadForm
from digits.models import Digits

def index(request):
    submitted = False
    if request.method == "POST":
        form = UploadForm(request.POST or None, request.FILES or None, )
        if form.is_valid():
            instance = form.save()
            messages.success(request, 'Item Added')
            instance = form.save()
            return redirect('prediction-result', instance.id)
    else:
        form = UploadForm
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted, }
    return render(request, 'index.html', context)

def predicted_image(request, id):
    image = Digits.objects.get(id=id)
    context = {
        'image': image
    }
    return render(request, 'predicted.html', context)
