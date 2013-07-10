from django.contrib import admin
from groceries.models import Category, Unit, Item, GroceryList, ListItem

admin.site.register(Category)
admin.site.register(Unit)
admin.site.register(Item)
admin.site.register(GroceryList)
admin.site.register(ListItem)