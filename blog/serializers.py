from rest_framework import serializers
from .models import BlogModel, CategoryModel, UserModel

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'email', 'username') 


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        """
        Check if the email is valid and ends with @redberry.ge
        """
        if not value.endswith('@redberry.ge'):
            raise serializers.ValidationError("Email must end with @redberry.ge")
        return value
