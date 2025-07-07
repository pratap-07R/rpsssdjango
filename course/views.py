from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from . models import *
from . serlializers import *

class rpsSignupUser(APIView): 
    def post(self,request):
        userdata = rpsSignupSerliazer(data=request.data)
        if userdata.is_valid():
            rpsUser.objects.create(**userdata.data)
            message = {"message": " user created successfully"}
            return JsonResponse(message,status=status.HTTP_201_CREATED)
        return JsonResponse(userdata.errors,status=status.HTTP_400_BAD_REQUEST)
    
class rpsGetUserDetails(APIView):
    def get(self,request):
        result = list(rpsUser.objects.filter().values())
        return JsonResponse(result,status=status.HTTP_200_OK, safe=False)

class rpsUpdateEmail(APIView):
    def put(self,request):
        userdata = rpsUpdateEmailSerliazer(data = request.data)
        if userdata.is_valid():
            email = userdata.data["email"]
            number = userdata.data["number"]
            rpsUser.objects.filter(number = number).update(email=email)
            message = {"message": "email update successfully"}
            return JsonResponse(message,status=status.HTTP_200_OK)
        return JsonResponse(userdata.errors,status=status.HTTP_400_BAD_REQUEST)

class rpsDeleteUser(APIView):
    def delete(self,request,number):
        rpsUser.objects.filter(number=number).delete()
        message = {"message": " user deleted successfully"}
        return JsonResponse(message, status=status.HTTP_204_NO_CONTENT)