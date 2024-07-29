from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import CategorySerializer, MenuItemSerializer, CartSerializer, OrderSerializer, UserSerilializer

class ManagerGroupViewSet(viewsets.ViewSet):
    permission_classes = [IsAdminUser]
    def list(self, request):
        users = User.objects.all().filter(groups__name='Manager')
        items = UserSerilializer(users, many=True)
        return Response(items.data)

    def create(self, request):
        user = get_object_or_404(User, username=request.data['username'])
        managers = Group.objects.get(name="Manager")
        managers.user_set.add(user)
        return Response({"message": "user added to the manager group"}, 200)

    def destroy(self, request):
        user = get_object_or_404(User, username=request.data['username'])
        managers = Group.objects.get(name="Manager")
        managers.user_set.remove(user)
        return Response({"message": "user removed from the manager group"}, 200)
    
class DeliveryGroupViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self,request):
        delivery_ppl=User.objects.all().filter(groups__name="Delivery Crew")
        items=UserSerilializer(delivery_ppl,many=True)
        return Response(items.data)
    
    def create(self,request):
        person=get_object_or_404(User,username=request.data["username"])
        delivery_persons=Group.objects.get(name="Delivery Crew")
        delivery_persons.user_set.add(person)
        return Response({"message": "user removed from the delivery group"}, 200)

    def destroy(self,request):
        person=get_object_or_404(User,username=request.data["username"])
        delivery_persons=Group.objects.get(name="Delivery Crew")
        delivery_persons.user_set.remove(person)
        return Response({"message": "user removed from the delivery group"}, 200)


@api_view()
@permission_classes([IsAuthenticated])
def secret_message(request):
    if request.user.groups.filter(name="Manager").exists():
        return Response("yeet")
    else:
        return Response({"no go"},403)
