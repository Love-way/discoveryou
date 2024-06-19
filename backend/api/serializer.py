from api.models import User, Profile
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # These are claims, you can add custom claims
        token['nom_enfant'] = user.profile.nom_enfant
        token['username'] = user.username
        token['age_enfant'] = user.profile.age_enfant
        token['email'] = user.email
        # token['type'] = user.profile.type
        token['genre'] = user.profile.genre
        token['ville_residence'] = user.profile.ville_residence
        token['ville_naissance'] = user.profile.ville_naissance
        token['ecole'] = user.profile.ecole
        token['classe'] = user.profile.classe
        token['image'] = str(user.profile.image)
        token['verified'] = user.profile.verified
        # ...
        return token

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('nom_enfant', 'age_enfant', 'email', 'genre', 'ville_residence', 'ville_naissance','ecole','classe', 'image', 'verified')



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    # type = serializers.CharField(required=True) 

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        
        # Validate 'type' field
        # if attrs['type'] not in ['Educateur', 'Parent']:
        #     raise serializers.ValidationError(
        #         {"type": "Invalid type. Please choose either 'Educateur' or 'Parent'."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        
        # **No need to create a Profile instance here anymore, as it's done in the view.**
        # # Create a Profile instance with the provided type
        # profile = user.profile
        # profile.type = validated_data['type']
        # profile.save()

        return user
    
# crud
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'