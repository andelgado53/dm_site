from django.contrib import admin
from reporting.models import Categories, Tables

# Register your models here.
class CategoriesAdmin(admin.ModelAdmin):

	list_display = ('name', 'description', 'deleted')
	list_display_links = ('name',)
	list_per_page = 30
	search_fields = ['name', 'description']

admin.site.register(Categories, CategoriesAdmin)

class TablesAdmin(admin.ModelAdmin):

	list_display = ('name', 'description', 'category','deleted')
	list_display_links = ('name',)
	list_per_page = 30
	search_fields = ['name', 'description']	

admin.site.register(Tables, TablesAdmin)