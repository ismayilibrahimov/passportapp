from django.db.models.query import QuerySet
from rest_framework.relations import PrimaryKeyRelatedField
from .models import Passport, Customer
from rest_framework import serializers


class PassportSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Passport
        fields = '__all__'
        read_only_fields = ('customer', )


class CustomerSerializer(serializers.ModelSerializer):
    passports = PassportSerializer(many=True)

    class Meta:
        model = Customer
        fields = '__all__'

    def create(self, validated_data):
        passports = validated_data.pop('passports')
        customer = Customer.objects.create(**validated_data)
        for passport in passports:
            Passport.objects.create(**passport, customer=customer)
        return customer

    def update(self, instance, validated_data):
        if validated_data.get('passports'):
            passports = validated_data.pop('passports')
            instance.name = validated_data.get('name', instance.name)
            instance.surname = validated_data.get('surname', instance.surname)
            instance.email = validated_data.get('email', instance.email)
            instance.phone = validated_data.get('phone', instance.phone)
            instance.save()
            keep_passports = []
            existing_ids = [p.id for p in instance.passports.all()]
            for passport in passports:
                if "id" in passport.keys():
                    if Passport.objects.filter(id=passport["id"]).exists():
                        print('movcud passporta duzelisin icinde')
                        p = Passport.objects.get(id=passport["id"])
                        p.scan_file = passport.get('scan_file', p.scan_file)
                        p.document_number = passport.get(
                            'document_number', p.document_number)
                        p.first_name = passport.get('first_name', p.first_name)
                        p.last_name = passport.get('last_name', p.last_name)
                        p.patronymic = passport.get('patronymic', p.patronymic)
                        p.nationality = passport.get(
                            'nationality', p.nationality)
                        p.birth_date = passport.get('birth_date', p.birth_date)
                        p.personal_number = passport.get(
                            'personal_number', p.personal_number)
                        p.gender = passport.get('gender', p.gender)
                        p.issue_date = passport.get('issue_date', p.issue_date)
                        p.expire_date = passport.get(
                            'expire_date', p.expire_date)
                        p.issuing_authority = passport.get(
                            'issuing_authority', p.issuing_authority)
                        p.save()
                        keep_passports.append(p.id)
                    else:
                        continue
                else:
                    p = Passport.objects.create(**passport, customer=instance)
                    keep_passports.append(p.id)
        else:
            instance.name = validated_data.get('name', instance.name)
            instance.surname = validated_data.get('surname', instance.surname)
            instance.email = validated_data.get('email', instance.email)
            instance.phone = validated_data.get('phone', instance.phone)
            instance.save()

        return instance
