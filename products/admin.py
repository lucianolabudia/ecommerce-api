from django.contrib import admin
from .models import Category, Size, Color, Product, ProductVariant

# Clase de administración personalizada para categoría
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'description')
    list_filter = ('parent',)
    search_fields = ('name','description')

# Desregistrar el valor predeterminado y registrarlo con la clase personalizada.
admin.site.register(Category, CategoryAdmin)

# Modelos registrados
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Product)
admin.site.register(ProductVariant)

