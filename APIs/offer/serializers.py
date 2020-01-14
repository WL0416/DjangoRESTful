from rest_framework import serializers
from .models import Offer

class OfferSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Offer
        fields = ['id','first_name','last_name','birthday','passport','phone','email', 'address', 'start_date', 'courses','campus']

    # id = serializers.IntegerField(read_only=True)
    # first_name = serializers.CharField(required=True, max_length=30)
    # last_name = serializers.CharField(required=False, max_length=30)
    # birthday = serializers.DateField(required=True)
    # passport = serializers.CharField(required=True, max_length=30)
    # phone = serializers.CharField(required=False, max_length=30)
    # email = serializers.EmailField(required=False, max_length=50)
    # address = serializers.CharField(required=True, max_length=150)
    # start_date = serializers.DateField(required=True)
    # courses = serializers.CharField(required=True, max_length=20)
    # campus = serializers.CharField(required=True, max_length=15)

    # def create(self, validated_data):
    #     return Offer.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.birthday = validated_data.get('birthday', instance.birthday)
    #     instance.passport = validated_data.get('passport', instance.passport)
    #     instance.phone = validated_data.get('phone', instance.phone)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.address = validated_data.get('address', instance.address)
    #     instance.start_date = validated_data.get('start_date', instance.start_date)
    #     instance.courses = validated_data.get('courses', instance.courses)
    #     instance.campus = validated_data.get('campus', instance.campus)
    #     instance.save()
    #     return instance
