
# Register your models here.
from django.contrib import admin
from restaurants.models import Restaurant, Food,Comment
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'address','date')
    search_fields = ('name',) 
    
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'price','is_spicy','comment','date')
    list_filter = ('is_spicy',)
    #fields = ('price','restaurant')
    search_fields = ('name',) 
    ordering = ('-price',)

admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Food,FoodAdmin)
admin.site.register(Comment)