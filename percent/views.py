from django.shortcuts import render
from django.http import HttpResponse


def response(context):
    return render(context, 'index.html')


async def index(request):
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
            "percent": percent
        }
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')
    # return HttpResponse("successfully")


