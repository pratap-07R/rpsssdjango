from rest_framework import serializers

class rpsSignupSerliazer(serializers.Serializer):
    userName = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    number = serializers.IntegerField()
    password = serializers.CharField(max_length=20)
    userType = serializers.CharField(max_length=20,)
    gender = serializers.CharField(max_length=10 , allow_null=True , allow_blank=True)

class rpsUpdateEmailSerliazer(serializers.Serializer):
    email = serializers.EmailField()
    number = serializers.IntegerField()
