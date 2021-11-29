from rest_framework.routers import DefaultRouter
from django.urls import path
from . import viewsets

app_name = "rooms"

<<<<<<< HEAD
urlpatterns = [
    path("list/", views.ListRoomsView.as_view()),
    path("<int:pk>/", views.SeeRoomView.as_view()),
]
=======
router = DefaultRouter()
router.register("", viewsets.RoomViewset, basename="room")

urlpatterns = router.urls
>>>>>>> a99aba80d28f5c537ddc3e9700d7328f862522f0
