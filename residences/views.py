from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

class HelloResidencesView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"message": "Hello Residences"}, status=status.HTTP_200_OK)

