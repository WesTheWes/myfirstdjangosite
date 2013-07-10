from django.contrib import admin
from recipes.models import Recipe, RecipeList

class RecipeAdmin(admin.ModelAdmin):
    filter_horizontal = ('ingredients',)

admin.site.register(RecipeList)
admin.site.register(Recipe, RecipeAdmin)