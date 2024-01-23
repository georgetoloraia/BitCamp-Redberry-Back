# from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from .models import BlogModel, CategoryModel, UserModel
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from .serializers import BlogListSerializer, BlogSerializer, CategorySerializer, UserSerializer, LoginSerializer
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from .filters import CategoryFilter


class BlogListView(generics.ListAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogListSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter

    def get_queryset(self):
        """
        Optionally restricts the returned blog posts to a given category,
        by filtering against a `category` query parameter in the URL.
        """
        queryset = super().get_queryset()
        category = self.request.query_params.get('category', None)
        if category is not None:
            queryset = queryset.filter(categories__id=category)
        return queryset

class BlogCreateView(generics.CreateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        print(request.data)  # Print the incoming data
        return super().post(request, *args, **kwargs)

class BlogDetailView(generics.RetrieveAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogListSerializer
    permission_classes = [AllowAny]

class CategoryListView(generics.ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

class UserCreateView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Allow any user (authenticated or not) to access this view

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            if not email.endswith('@redberry.ge'):
                return Response({'error': 'Email must end with @redberry.ge'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


User = get_user_model()

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]  # Allow any user (authenticated or not) to access this view

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']

            # Check if email ends with @redberry.ge
            if not email.endswith('@redberry.ge'):
                return Response({'error': 'Email must end with @redberry.ge'}, status=status.HTTP_400_BAD_REQUEST)

            # Get or create user
            user, created = User.objects.get_or_create(email=email)
            if created:
                user.username = email.split('@')[0]  # Optional: Create a username from the email
                user.save()

            # Get or create token
            token, _ = Token.objects.get_or_create(user=user)

            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
