from django.db import models
import mysite.groceries

class Recipe(models.Model):
	recipe_name = models.CharField(max_length=50)
	ingredients = models.ManyToMany(groceries.Ingredient)
	servings = models.integerField()
	Calories = models.FloatField()
	
	def __unicode__(self):
		return self.recipe_name