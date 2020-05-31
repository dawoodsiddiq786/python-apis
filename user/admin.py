from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

# Register your models here.
admin.site.site_header = 'Huey\'s List App Admin Panel'



class UserShow(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',)
    list_filter = ('date_joined', )


admin.site.register(User, UserShow)




class CategoryShow(admin.ModelAdmin):
    list_display = ('name', 'description', 'created',)
    list_filter = ('created', )


admin.site.register(Categorie, CategoryShow)



admin.site.register(Media)


class ProductShow(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at',)
    list_filter = ('created_at', )


admin.site.register(Product, ProductShow)







class UserPostShow(admin.ModelAdmin):
    list_display = ('posted_by', 'description', 'created_at',)
    list_filter = ('created_at', )


admin.site.register(Post, UserPostShow)
admin.site.register(Comment)