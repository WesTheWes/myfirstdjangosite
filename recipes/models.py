from django.db import models
import groceries

class Recipe(models.Model):
	recipe_name = models.CharField(max_length=30)
	ingredients = models.ManyToManyField('groceries.ListItem')
	servings = models.IntegerField()
	calories = models.FloatField()
	
	def __unicode__(self):
		return self.recipe_name

class RecipeList(models.Model):
	recipe_name = models.CharField(max_length=30)
	recipe = models.ManyToManyField(Recipe)

	def __unicode__(self):
		return self.list_name