from rest_framework import serializers
from django.utils import timezone
import datetime
from django.contrib.auth import get_user_model
from rest_framework_jwt.settings import api_settings
from django.conf import settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler=api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
expire_delta=settings.JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA']
User=get_user_model()
class UserRegisterSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    token=serializers.SerializerMethodField(read_only=True)
    expire = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model=User
        fields= [
            'username',
            'email',
            'password',
            'password2',
            'token',
            'expire'
        ]
        extra_kwargs={"password":{"write_only":True}}
    def get_expire(self,obj):
        return  timezone.now()+expire_delta-datetime.timedelta(seconds=200)
    def get_token(self,obj):
        user=obj

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token

    def validate(self,data):
            pw=data.get('password')
            pw2 = data.pop('password2')
            if pw!=pw2:
                raise serializers.ValidationError("password must match")
            return data
    def validate_email(self,value):
        qs = User.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError('User with this email already exist')
        return value
    def validate_username(self,value):
        qs=User.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError('User with this Username already exist')

        return value

    def create(self,validated_data):
            user_obj=User(
                username=validated_data.get("username"),
                email=validated_data.get("email"),

            )
            user_obj.set_password(validated_data.get("password"))
            user_obj.save()
            return user_obj