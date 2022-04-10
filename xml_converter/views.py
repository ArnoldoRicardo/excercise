from django.http import JsonResponse
from django.shortcuts import render

from .forms import FileForm
from .xml2json import xml2json


def upload_page(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            response = xml2json(request.FILES['file'])
            return JsonResponse(response, content_type='application/json')
    else:
        form = FileForm()

    return render(request, "upload_page.html", {'form': form})
