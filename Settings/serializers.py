from rest_framework import serializers
from Accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ='__all__'
        extra_kwargs = {"password": {'write_only': True}}
        def create(self, validated_data):
            """create and return a new user."""
            user = User(
                email = validated_data["email"],
                username = validated_data["username"],
                photoProfile = validated_data["photoProfile"],
                tel1 = validated_data["tel1"],
                tel2 = validated_data["tel2"],
                dateNaissance = validated_data["dateNaissance"],
                adresse = validated_data["adresse"],
                url_linkedIn = validated_data["url_linkedIn"],
                genre = validated_data["genre"],
                ville = validated_data["ville"],
                country = validated_data["country"],

            )
            user.set_password(validated_data["password"])
            user.save()
            return user
