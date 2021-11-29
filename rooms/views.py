from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Room
from .serializers import RoomSerializer, BigRoomSerializer


class ListRoomsView(ListAPIView):

    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class SeeRoomView(RetrieveAPIView):

    queryset = Room.objects.all()
<<<<<<< HEAD
    serializer_class = RoomSerializer
=======
    serializer_class = BigRoomSerializer
>>>>>>> a99aba80d28f5c537ddc3e9700d7328f862522f0
