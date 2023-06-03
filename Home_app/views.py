from django.shortcuts import redirect
from .models import *
from django.contrib.auth import authenticate,logout,login
from .serializers import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics ,response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser ,JSONParser
import random
from rest_framework.response import Response
from rest_framework.decorators import api_view,parser_classes
from .mixins import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken


@method_decorator(csrf_exempt, name='dispatch')
class Register(APIView):
    serializer_class = RegisterSerializer
    parser_classes = (MultiPartParser, FormParser,JSONParser)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            user = CustomUser.objects.get(username = serializer.data['username'])
            refresh = RefreshToken.for_user(user)
            return Response( {'id':str(user.id),'refresh': str(refresh),'access': str(refresh.access_token),'message':"Register successfully"},status=status.HTTP_201_CREATED)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST'])
@parser_classes([JSONParser,FormParser,MultiPartParser])
def login_view(request):
    if request.method =='POST':
        mobile =request.POST.get('mobile')
        user = CustomUser.objects.get(mobile=mobile)
        # if not user.exists():
        #     return response.Response(status=status.HTTP_400_BAD_REQUEST)
        
        print(user)
        user.otp = random.randint(1000,9999)
        print(user.otp)
        user.save()
        # send_otp_on_phone(mobile,user.otp)

        return Response({'uid': str(user.uid),'message':"Otp send successfully"})
    return response.Response(status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
@parser_classes([JSONParser,FormParser,MultiPartParser])
def otp(request,uid):
    if request.method =='POST':
        otp = request.POST.get('otp')
        profile = CustomUser.objects.get(uid=uid)
        print(profile)
        if otp == profile.otp:
            print(profile.otp)
            login(request,profile)
            refresh = RefreshToken.for_user(profile)
            return Response({'user': profile.email,'id':str(profile.id),'refresh': str(refresh),'access': str(refresh.access_token),'message':"Login successfully"})

    return response.Response(status=status.HTTP_400_BAD_REQUEST)