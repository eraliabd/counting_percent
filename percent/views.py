import os.path
import uuid

# import win32com.client
# import comtypes.client

from django.http import HttpResponse
from django.shortcuts import render
from .models import Percent
# from docx2pdf import convert


def home(request):
    return render(request, 'home.html')


def index(request):
    if request.method == 'POST':
        number = int(request.POST.get('number', ''))
        percent = int(request.POST.get('percent', ''))

        percent_value = (number * percent) / 100
        residual_value = number - percent_value
        value_increase = number + percent_value

        context = {
            "percent_value": percent_value,
            "residual_value": residual_value,
            "value_increase": value_increase,
            "number": number,
            "percent": percent
        }
        model = Percent()
        model.number = number
        model.percent = percent
        model.percent_value = percent_value
        model.residual_value = residual_value
        model.value_increase = value_increase
        model.save()

        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')


# def converter(request):
#     if request.method == 'POST':
#         file_input = request.FILES.get('docs', '')
#         print("input file:", file_input)
#         pdf = f"pdf_{str(uuid.uuid4()).split('-')[-1]}.pdf"
#         file_output = os.path.abspath(f"files/pdf_files/{pdf}")
#         print("file output:", file_output)
#
#         word = win32com.client.Dispatch('Word.Application')
#         doc = word.Documents.Open(file_input)
#         print("Doc: ", doc)
#         doc.SaveAs(file_output, FileFormat=17)
#         doc.Close()
#         word.Quit()
#         with open(os.path.abspath(f"files/pdf_files/{pdf}"), 'rb') as file:
#             file = file.read()
#
#     # if str(input_doc).endswith(".doc"):
#             return render(request, 'doc_to_pdf.html', {"pdf_file": file})
#     else:
#         return render(request, 'doc_to_pdf.html')
