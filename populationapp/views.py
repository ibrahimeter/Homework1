from django.shortcuts import render
from populationapp import models
from .models import Customuser
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@csrf_exempt
def customuser(request):
    print(request.method)
    if request.method == "GET":
        listdata = [] 
        for customuser in  Customuser.objects.all():
            my_data =customuser.serialize()
            listdata.append(my_data)
    
        all_data = {"customuser": listdata}
    else:
        data = json.loads(request.body)
        first_name = data["first_name"]
        last_name = data["last_name"]
        email = data["email"]
        customuser = Customuser(first_name = first_name,last_name=last_name,email=email)
        customuser.save()
        all_data = {"customuser": customuser.serialize}


    return JsonResponse(all_data)