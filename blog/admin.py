from django.contrib import admin
from .models import BlogModel, CategoryModel, UserModel



# Register your models with the customized admin classes
admin.site.register(BlogModel)
admin.site.register(CategoryModel)
admin.site.register(UserModel)
