from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from points.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    renderer_classes = [TemplateHTMLRenderer]

    def list(self, request, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"data": serializer.data}, template_name="home.html")

    def retrieve(self, request, pk=None, **kwargs):
        queryset = self.get_queryset()
        user = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(user)
        return Response({"data": serializer.data},  template_name="user.html")

    def update(self, request, pk=None, **kwargs):
        queryset = self.get_queryset()
        user = get_object_or_404(queryset, pk=pk)
        user.profile.points = request.data.get("points")
        user.profile.save()
        serializer = self.get_serializer(user)
        return Response({"data": serializer.data}, template_name="user.html")

