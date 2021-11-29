from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Room


class RoomSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Room
<<<<<<< HEAD
        exclude = ("modified",)
=======
        fields = (
            "pk",
            "name",
            "price",
            "instant_book",
            "user",
        )


class BigRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        exclude = ()
>>>>>>> a99aba80d28f5c537ddc3e9700d7328f862522f0
