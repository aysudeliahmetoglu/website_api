from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from .models import Events

# Create your views here.


class deneme(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permissions_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response("test")


class CreateEvent(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permissions_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            Events.objects.create(
                user=request.user, name=request.data['name'], date=request.data['date'])
        except:
            return Response("", status=status.HTTP_404_NOT_FOUND)
        return Response("", status=status.HTTP_201_CREATED)


class ListEvents(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permissions_classes = [permissions.IsAuthenticated]

    def get(self, request):
        qs = Events.objects.all()
        return Response(qs.values())


class DeleteEvents(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permissions_classes = [permissions.IsAuthenticated]

    def delete(self, request, id):
        obj = get_object_or_404(Events, id=id)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
