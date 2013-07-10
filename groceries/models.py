from django.db import models
from django.contrib.auth.models import User
import re

class Category(models.Model):
	# A list of all categories
	category_name = models.CharField(max_length=30, unique=True)
	
	def __unicode__(self):
		return self.category_name

class Unit(models.Model):
	# A list of all units, with one blank for items with no units
	# Make sure all units are singular (e.g. ounce, pound, liter)
	unit_type = models.CharField(max_length=30, blank=True, unique=True)
	
	def __unicode__(self):
		if self.unit_type:
			return self.unit_type
		else:
			return u'No Units'

class Item(models.Model):
	# This is a list of all items
	# Make sure all items are singular
	item = models.CharField(max_length=30, unique=True)
	price = models.FloatField(blank=True)
	unit = models.ForeignKey(Unit, default=Unit.objects.get(unit_type=""))
	category = models.ForeignKey(Category, blank=True, null=True)
	calories = models.FloatField(default=0)
	
	def __unicode__(self):
		return self.item
	
class ListItem(models.Model):
	# Each item in a recipe or grocery list will be put through here
	# Allows the amount of each item to be saved in the database, and associated with a Recipe
	item_name = models.ForeignKey(Item, blank=True, null=True)
	amount = models.FloatField()
	
	def __unicode__(self):
		# checks to see if there is a unit, if the amount is more than 1, and then prints the amount of the item
		if self.amount > 1:
			def pluralize(x):
				return plural(x)
		else:
			def pluralize(x):
				return x
		item = (self.item_name.unit.unit_type and 
		        u'%s of %s' %(pluralize(self.item_name.unit.unit_type), self.item_name.item) or 
				u'%s' %pluralize(self.item_name.item))
		return u'%s %s' %(self.amount, item)

class GroceryList(models.Model):
	list_name = models.CharField(max_length=30)
	recipes = models.ManyToManyField('recipes.RecipeList', blank=True, null=True)
	additional_items = models.ManyToManyField(ListItem, blank=True, null=True)
	total_price = models.FloatField(default=0)
	user = models.ForeignKey(User)
	
	def __unicode__(self):
		return self.list_name

def plural(noun):                            
    if re.search('[sxz]$', noun):             
        return re.sub('$', 'es', noun)        
    elif re.search('[^aeioudgkprt]h$', noun):
        return re.sub('$', 'es', noun)       
    elif re.search('[^aeiou]y$', noun):      
        return re.sub('y$', 'ies', noun)     
    else:                                    
        return noun + 's'   