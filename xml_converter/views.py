from django.http import JsonResponse
from django.shortcuts import render

from .forms import FileForm
from .xml_to_json import convert_file


def upload_page(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            response = convert_file(request.FILES['file'])
            return JsonResponse(response)

    else:
        form = FileForm()

    return render(request, "upload_page.html", {'form': form})
