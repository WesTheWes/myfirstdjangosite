from django.db import models
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

class Ingredient(models.Model):
	ingredient_name = models.CharField(max_length=30)
	price = models.FloatField()
	unit = models.ForeignKey(Unit)
	category = models.ForeignKey(Category)
	amount = models.FloatField()
	calories = models.IntegerField()
	
	def __unicode__(self):
		# checks to see if there is a unit
		ingredient = (self.unit.unit_type and 
		              u'%s of %s' %(plural(self.unit.unit_type), self.ingredient_name) or 
					  u'%s' %plural(self.ingredient_name))
		return u'%s %s' %(self.amount, ingredient)

def plural(noun):                            
    if re.search('[sxz]$', noun):             
        return re.sub('$', 'es', noun)        
    elif re.search('[^aeioudgkprt]h$', noun):
        return re.sub('$', 'es', noun)       
    elif re.search('[^aeiou]y$', noun):      
        return re.sub('y$', 'ies', noun)     
    else:                                    
        return noun + 's'   