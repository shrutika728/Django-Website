from django.contrib import admin
from app1.models import Contact
# Register your models here.
class Contactadmin(admin.ModelAdmin):
	list_display=['Name','Phone','Email','Message']
admin.site.register(Contact,Contactadmin)
