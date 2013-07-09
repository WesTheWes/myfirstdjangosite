from django.db import models
import mysite.groceries
import mysite.users

class Recipe(models.Model):
	recipe_name = models.CharField(max_length=30)
	ingredients = models.ManyToMany(groceries.Ingredient)
	servings = models.integerField()
	Calories = models.FloatField()
	
	def __unicode__(self):
		return self.recipe_name

class RecipeList(models.Model):
	
	recipe_name = models.CharField(max_length=30)
	recipe = models.ForeignKey(Recipe)
	
	def __unicode__
		return self.list_name