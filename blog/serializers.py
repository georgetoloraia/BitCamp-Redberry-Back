from rest_framework import serializers
from .models import BlogModel, CategoryModel, UserModel

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id', 'title', 'text_color', 'background_color']

class BlogListSerializer(serializers.ModelSerializer):

    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = BlogModel
        fields = ['id', 'title', 'author', 'publish_date', 'description', 'image', 'email', 'categories']
        # read_only_fields = ('id', 'image')


class BlogSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)

    class Meta:
        model = BlogModel
        fields = '__all__'

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        blog = BlogModel.objects.create(**validated_data)
        for category_data in categories_data:
            category, created = CategoryModel.objects.get_or_create(**category_data)
            blog.categories.add(category)
        return blog

    # def update(self, instance, validated_data):
    #     categories_data = validated_data.pop('categories')
    #     categories = (instance.categories).all()
    #     categories = list(categories)
    #     instance.title = validated_data.get('title', instance.title)
    #     # ... handle other fields ...
    #     instance.save()

    #     for category_data in categories_data:
    #         category = categories.pop(0)
    #         category.title = category_data.get('title', category.title)
    #         category.text_color = category_data.get('text_color', category.text_color)
    #         category.background_color = category_data.get('background_color', category.background_color)
    #         category.save()
    #     return instance



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
