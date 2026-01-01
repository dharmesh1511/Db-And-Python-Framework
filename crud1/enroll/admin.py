from django.contrib import admin
from .models import User,Doctor,Item

# admin penal changes
admin.site.site_header = "My Custom Admin"
admin.site.site_title = "My Admin Portal"
admin.site.index_title = "Welcome to My Admin Dashboard"


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_dispaly=('id','name','email','password')


@admin.register(Doctor)
class StudentAdmin(admin.ModelAdmin):
    list_dispaly=('id','name','age','grade','email')

    # list_dispaly=['id','name','age','grade','email']  #display in list

    search_fields = ('name', 'email') #search karne ke liye

    list_filter = ('age',) # filter by age 

    class Media:
        css = {
            'all': ('admin/css/custom.css',)
        }
        js = ('admin/js/custom.js',)




@admin.register(Item)
class itemAdmin(admin.ModelAdmin):
    list_dispaly=('id','name','description')