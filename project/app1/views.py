from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .emails import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


'''
RegisterAPI view where userserializer stores in a variable 'serializer' where we are checking
if it is valid or not .
'''

class RegisterAPI(APIView):
    def post(self, request):  
            data=request.data
            serializer=Userserializer(data=data)
            if serializer.is_valid():
                serializer.save()
                otp(serializer.data['email'])
                return Response({
                    'message':'registration successfully check your mail',
                    'data': serializer.data,
                })
            return Response({
                'message':'something went wrong',
                'data': serializer.errors
            })   


'''
in LoginAPI where Loginserializer stores in a variable 'serializer'. and we stores email 
in 'email' and password in 'password' variable and then authenticate it and also we have
used RefreshToken as well 
'''

class LoginAPI(APIView):
    def post(self,request):
        try:
            data=request.data
            serializer=Loginserializer(data=data)
            if serializer.is_valid():
                email=serializer.data['email']
                password=serializer.data['password']
                user=authenticate(email=email,password=password)
                if user is None:
                    return Response({
                        'message':'invalid password',
                        'data':{}
                    })

                refresh = RefreshToken.for_user(user)
                return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                })
            
            return Response({
                'message':'something went wrong',
                'data':serializer.errors
            })
        except Exception as e:
            print(e)



class OTPverify(APIView):
    def post(self, request):
        try:
            data=request.data
            serializer=Accountverifyserializer(data=data)
            if serializer.is_valid():
                email=serializer.data['email']
                otp=serializer.data['otp']
                user=User.objects.filter(email=email)
                if not user.exists:
                     return Response({
                     'message':'something went wrong',
                     'data': 'invalid Email'
                })
                if user[0].otp != otp:
                     return Response({
                     'message':'something went wrong',
                     'data': 'wrong otp'
                })
                user=user.first()
                user.is_varified=True
                user[0].save()
                return Response({
                    'message':'account verified',
                    'data': {}
                })
            return Response({
                'message':'something went wrong',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)
