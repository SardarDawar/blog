from django.contrib import admin
from django.shortcuts import render,redirect
from .models import code_post,BlogAuthor,Category,example

class code_postAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display=['title','publish' ]
  

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('Name',)}





admin.site.register(code_post,code_postAdmin)
admin.site.register(BlogAuthor)
admin.site.register(example)
admin.site.register(Category,CategoryAdmin)



