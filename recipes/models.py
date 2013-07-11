from django.db import models
from django.contrib.auth.models import User
import groceries

class Recipe(models.Model):
	recipe_name = models.CharField(max_length=30)
	ingredients = models.ManyToManyField('groceries.ListItem')
	servings = models.FloatField(blank=True, null=True)
	user = models.ForeignKey(User)
	
	def calories(self):
		calories = 0
		for ingredient in self.ingredients:
			calories += (ingredient.item_name.calories * ingredient.amount)
		return calories
	
	def __unicode__(self):
		return self.recipe_name

class RecipeList(models.Model):
	recipe_name = models.CharField(max_length=30)
	recipe = models.ManyToManyField(Recipe)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.list_name