from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api_app import models
from api_app.serializers import *


# Create your views here.

@api_view(['GET'])
def home(request):
    data = models.User.objects.all()
    serializer = UserSerializer(data, many=True)
    return Response({'status': 200, "payload": serializer.data})


@api_view(['POST'])
def post_data(request):
    serializer = UserSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'status': 403, 'errors': serializer.errors, 'messgae': 'Something went wrong'})

    serializer.save()
    return Response({'status': 200, "payload": serializer.data, 'messgae': 'You Sent'})


def createitem():
    for i in range(10):
        models.User.objects.create(name='suprit', city='Bnglr', state='Ktk', about='Good', status='Active')
        print(i)


# createitem()

@api_view(['PUT'])
def updateUser(request, id):
    try:
        user_obj = models.User.objects.get(user_id=id)
        serializer = UserSerializer(user_obj, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'messgae': 'Something went wrong'})

        serializer.save()
        return Response({'status': 200, "payload": serializer.data, 'messgae': 'You Sent'})
    except Exception as e:
        print(e)
        return Response({'status': 403, 'message': 'Invalid Id'})


@api_view(['DELETE'])
def deleteUser(request, id):
    try:
        user_obj = models.User.objects.get(user_id=id)
        user_obj.delete()
        return Response({'status': 200, 'messgae': 'Deleted Successfully'})
    except Exception as e:
        print(e)
        return Response({'status': 403, 'message': 'Invalid Id'})
