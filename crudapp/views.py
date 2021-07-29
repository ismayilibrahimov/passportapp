from rest_framework import viewsets
from rest_framework.response import Response
from . import models
from . import serializers
from django.utils import timezone


class CustomerViewset(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer

    def destroy(self, request, *args, **kwargs):
        customer = self.get_object()
        for passport in customer.passports.all():
            passport.deleted_at = timezone.now()
            passport.save()

        customer.deleted_at = timezone.now()
        customer.save()
        return Response({"message": "customer details deleted successfully!"})


class PassportViewset(viewsets.ModelViewSet):
    queryset = models.Passport.objects.all()
    serializer_class = serializers.PassportSerializer

    def destroy(self, request, *args, **kwargs):
        passport = self.get_object()
        passport.deleted_at = timezone.now()
        passport.save()
        return Response({"message": "passport details deleted successfully!"})
