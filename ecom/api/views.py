from django.http import JsonResponse

# Create your views here.


def home(request):
    return JsonResponse({
        "info": "DJango and React Project",
        "name": "Mir Ashiful Karim"
    })
