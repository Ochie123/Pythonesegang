from django.contrib import admin


from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = [ "title"]
    list_display_links = [ "title"]
    fieldsets = ((("Product"), {"fields": ("title", "slug", "description")}),)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Product, ProductAdmin)