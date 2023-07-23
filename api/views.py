from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Profile
from .serializers import ProfileSerializer

# Create your views here.


@api_view(["GET"])
def hello(request):
    world = {"Hello world!": "Welcome to Nostalgia API!"}
    return Response(world)


class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
