from django.db import models
import recipes
import re

class Category(models.Model):

	category_name = models.CharField(max_length=30)
	
	def __unicode__(self):
		return self.category_name

class Unit(models.Model):
	# Make sure all units are single (e.g. ounce, pound, liter)
	unit_type = models.CharField(max_length=30, blank=True)
	
	def __unicode__(self):
		if unit_type:
			return self.unit_type
		else:
			return u'No Units'

class Item(models.Model):
	item_name = models.CharField(max_length=30)
	price = models.FloatField()
	unit = models.ForeignKey(Unit)
	category = models.ForeignKey(Category)
	amount = models.FloatField(blank=True)
	calories = models.FloatField(blank=True)
	
	def __unicode__(self):
		# checks to see if there is a unit, and then prints the amount of the Ingredient
		item = (self.unit.unit_type and 
		              u'%s of %s' %(plural(self.unit.unit_type), self.item_name) or 
					  u'%s' %plural(self.item_name))
		return u'%s %s' %(self.amount, ingredient)

class GroceryList(models.Model):
	list_name = models.CharField(max_length=30)
	recipes = models.ManyToManyField('recipes.RecipeList')
	total_price = models.FloatField()
	
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