from django.contrib import admin
from apps.company.models import *
# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 10
    search_fields = ['name']
admin.site.register(Company, CompanyAdmin)

class StatisticAdmin(admin.ModelAdmin):
    list_display = ['name','count']
    list_per_page = 10
    search_fields = ['name']
admin.site.register(Statistic,StatisticAdmin) 

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name','about']
    list_per_page = 10
    search_fields = ['name']
admin.site.register(Service,ServiceAdmin)

class PositionAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 10
    search_fields = ['name']
admin.site.register(Position,PositionAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ['name','position']
    list_per_page = 10
    search_fields = ['name']
admin.site.register(Team,TeamAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['address','phone','facebook','instagram','telegram','linkedin']
    list_per_page = 10
    search_fields = ['address']
admin.site.register(Contact,ContactAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ['name','about','description','date','viewed']
    list_per_page = 10
    search_fields = ['name']
admin.site.register(Blog,BlogAdmin)
  

admin.site.register(About)