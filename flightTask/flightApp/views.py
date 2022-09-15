from flightApp.models import Flight,Passenger,Reservation
from flightApp.serializers import FlightSerializer,PassengerSerializer,ReservationSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
'''from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render
from rest_framework.authtoken.views import obtain_auth_token
'''

# Create your views here.

# @api_view(['GET','POST'])
# def reservation_operations(request):
#     if request.method=='POST':
        
class FlightViewSet(viewsets.ModelViewSet):
    queryset=Flight.objects.all()
    serializer_class=FlightSerializer
    filter_backends=[filters.OrderingFilter]
    ordering_fields=['id','dateOfDeparture','estimatedTimeOfDeparture']
    #permission_classes=[IsAuthenticated]

class PassengerViewSet(viewsets.ModelViewSet):
    queryset=Passenger.objects.all()
    serializer_class=PassengerSerializer
    filter_backends=[filters.OrderingFilter]
    ordering_fields=['id']

class ReservationViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer
    
# @api_view(['POST'])
# def save_reservation(request):
    
#     flight=Flight.objects.get(id=request.data['flightId'])
    
#     passenger=Passenger()
    
#     passenger.firstName=request.data['firstName']
#     passenger.lastName=request.data['lastName']
#     passenger.middleName=request.data['middleName']
#     passenger.email=request.data['email']
#     passenger.phone=request.data['phone']
    
#     passenger.save()
    
#     reservation=Reservation()
    
#     reservation.flight=flight
#     reservation.passenger=passenger
    
#     reservation.save()
    
#     return Response(status=status.HTTP_201_CREATED)

# @api_view(['POST'])
# def findflights(request):
#     flights=Flight.objects.filter(departureCity=request.data['departureCity'],arrivalCity=request.data['arrivalCity'],dateOfDeparture=request.data['dateOfDeparture'])
#     serializer=FlightSerializer(flights,many=True)
#     return Response(serializer.data)