from django.db import models
from django.contrib.auth.models import User
import groceries

class Direction(models.Model):
	step = models.CharField(max_length=200)

class Recipe(models.Model):
	recipe_name = models.CharField(max_length=30)
	ingredients = models.ManyToManyField('groceries.ListItem')
	servings = models.FloatField(blank=True, null=True)
	creator = models.ForeignKey(User)
	directions = models.ManyToManyField(Direction)
	
	def __unicode__(self):
		return self.recipe_name

	def calories(self):
		calories = 0
		for ingredient in self.ingredients:
			calories += ingredient.calories
		return calories
	
	def price(self):
		price = 0
		for ingredient in self.ingredients:
			price += ingredient.price
		return price
		
class RecipeList(models.Model):
	recipe_name = models.CharField(max_length=30)
	recipes = models.ManyToManyField(Recipe)
	
	def price(self):
		price = 0
		for recipe in self.recipes:
			price += recipe.price
		return price

	def __unicode__(self):
		return self.list_name