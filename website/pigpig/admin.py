from django.contrib import admin

# Register your models here.
from pigpig.models import part

# class partAdmin(admin.ModelAdmin):
#     list_display=('id','name','english','taste','cooking','recipename','recipename2','recipe','pic1','pic2','pic3','url1')
#     ordering=('id',)

class partAdmin(admin.ModelAdmin):
    list_display=('id','name','english','taste','cooking','recipename','recipename2','recipe','pic1','pic2','pic3','url')
    ordering=('id',)


admin.site.register(part,partAdmin)