from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.response import Response

class ProfileCreateList(generics.ListCreateAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer

    def post(self,request,*args,**kwargs):
        response=super().post(request,*args,**kwargs)
        return Response({"message":"Profile created"}, status=200)

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
