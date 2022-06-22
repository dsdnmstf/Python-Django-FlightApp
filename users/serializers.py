from rest_framework import serializers, validators
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class RegisterSeializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True,
        validators=[validators.UniqueValidator(queryset=User.objects.all())],
        )
    password = serializers.CharField(
        # write_only=True daunten
        required = True,
        validators = [validate_password],
        style = {"input_type" : "password"},
    )
    password2 = serializers.CharField(
        # write_only=True daunten
        required = True,
        validators = [validate_password],
        style = {"input_type" : "password"},
    )


    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
            "password2"
        )

        extra_kwargs = {
            "password" : {"write_only" : True},
            "password2" : {"write_only" : True}
        }

    def create(self, validated_data):
        password = validated_data.get("password")
        validated_data.pop("password2")
        user = user.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"] :
            raise serializers.ValidationError(
                {"message" : "Passwords didn't match!"}
            )
        return attrs
