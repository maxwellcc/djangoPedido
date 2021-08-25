from django.contrib import admin
from .models import Cliente, Pedido, ItemPedido, Vendedor, Produto

admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
admin.site.register(Vendedor)
admin.site.register(Produto)
