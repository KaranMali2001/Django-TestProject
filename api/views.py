from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializer import UserSerializer
@api_view(['GET'])
def get_users(request):
        users= User.objects.all()
        serialData= UserSerializer(users,many=True)
        return Response(serialData.data)

@api_view(['POST'])
def create_user(requset):
        serialData= UserSerializer(data=requset.data)
        if serialData.is_valid():
                serialData.save()
                return Response(serialData.data,status=status.HTTP_201_CREATED)
        return Response(serialData.errors,status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','PUT','DELETE'])
def user_deatils(request,pk):
        try:
                user=User.objects.get(pk=pk)
        except User.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        
        if request.method=='GET':
                serialData= UserSerializer(user)
                return Response(serialData.data)
        if request.method=='PUT':
                serialData= UserSerializer(user,data=request.data)
                if serialData.is_valid():
                        serialData.save()
                        return Response(serialData.data)        
                return Response(serialData.errors,status=status.HTTP_400_BAD_REQUEST)
        if request.method =='DELETE':
                user.delete()
                return Response(status=status.HTTP_200_OK)
          

