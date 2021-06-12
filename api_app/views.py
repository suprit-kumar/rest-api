import random
import string
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api_app import models
from api_app.serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['GET'])
def home(request):
    data = models.User.objects.all()
    serializer = UserSerializer(data, many=True)
    return Response({'status': 200, "payload": serializer.data})


class RegisterUser(APIView):
    def post(self, request):
        serializer = UsrSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'messgae': 'Something went wrong'})

        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        token_obj,_= Token.objects.get_or_create(user=user)
        return Response({'status': 200, "payload": serializer.data, 'token': str(token_obj), 'messgae': 'You Sent'})



class StudentAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        student_objs = models.Student.objects.all()
        serializer = StudentSerializer(student_objs, many=True)
        print(request.user)
        return Response({'status': 200, "payload": serializer.data})

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'messgae': 'Something went wrong'})

        serializer.save()
        return Response({'status': 200, "payload": serializer.data, 'messgae': 'You Sent'})

    def put(self, request):
        try:
            student_objs = models.Student.objects.get(id=request.data['id'])
            serializer = StudentSerializer(student_objs, data=request.data, partial=True)
            if not serializer.is_valid():
                return Response({'status': 403, 'errors': serializer.errors, 'messgae': 'Something went wrong'})

            serializer.save()
            return Response({'status': 200, "payload": serializer.data, 'messgae': 'Your data has updated'})
        except Exception as e:
            print(e)
            return Response({'status': 403, 'message': 'Invalid Id'})

    def delete(self, request):
        try:
            student_objs = models.Student.objects.get(id=request.data['id'])
            student_objs.delete()
            return Response({'status': 200, 'messgae': 'Deleted Successfully'})
        except Exception as e:
            print(e)
            return Response({'status': 403, 'message': 'Invalid Id'})


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


@api_view(['GET'])
def get_book(request):
    data = models.Book.objects.all()
    serializer = BookSerializer(data, many=True)
    return Response({'status': 200, "payload": serializer.data})


def createLocally():
    for i in range(1, 10):
        catgry = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
        # title = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
        # cat = models.Category.objects.create(category_name=catgry)
        # models.Book.objects.create(boot_title=title,category=models.Category.objects.get(id=cat.id))
        # models.Student.objects.create(name=catgry,father_name='SK')
        models.User.objects.update(username=catgry)
    print('created')

# createLocally()
