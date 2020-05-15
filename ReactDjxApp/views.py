from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

def hola(request):
    print("agarro")
    data = [ 
    {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    },
    {
        'name': 'sususu',
        'location': 'fff',
        'is_active': True,
        'count': 28
    }

    ]

    #datos = json.dumps(data)
    
    #datos = json.loads(data)

    return JsonResponse(data, safe=False)

