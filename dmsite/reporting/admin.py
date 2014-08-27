from django.contrib import admin
from reporting.models import Categories, Tables, gms_units, prm_plst_added

# Register your models here.
class CategoriesAdmin(admin.ModelAdmin):
	#creates a class to modfify the way the models shows in the admin

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
admin.site.register(gms_units) #registers the table in the admin module. 
admin.site.register(prm_plst_added)