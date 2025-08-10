from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    # jerarquía de categorias
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

class Product(models.Model):
    # Información general básica sobre el concepto del producto
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    categories = models.ManyToManyField(Category, related_name='products')

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=50, unique=True)
    hex_code = models.CharField(max_length=7, unique=True) # e.g., #FFFFFF

    def __str__(self):
        return self.name

class ProductVariant(models.Model):
    # The specific variant of a product
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    sku = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='product_variants/', blank=True, null=True)

    class Meta:
        # Garantiza que no se puedan tener dos variantes del mismo producto con el mismo tamaño y color exactos.
        unique_together = ('product', 'size', 'color')

    def __str__(self):
        return f'{self.product.name} - {self.size.name} - {self.color.name}'