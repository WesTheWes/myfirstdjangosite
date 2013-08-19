from django.shortcuts import render
from recipes.models import Recipe
from groceries.models import plural
import nltk
from django.http import Http404
# Create your views here.

def parse_ingredient(string): # Parses an input string into a tuple in the form of (item_name, amount, unit) ready to be saved as a list item.
	pass

def create_recipe(request):
	errors = []
	new_ingredient={}
	new_direction=''
	if 'new_recipe' not in request.session: # If this user has not already tried to create a recipe, one is created when they visit the site.
		recipe = Recipe()
		recipe.save()
		new_recipe = recipe.id
		request.session['new_recipe'] = new_recipe # The 'new_recipe' cookie is the ID of the saved recipe, should be reset when the recipe is saved or erased.
		ingredients=[]
		directions=[]
		recipe_name = 'Recipe Name'
		errors.append('New Recipe %s created with ID %s' %(recipe_name, new_recipe))
		new_ingredient={'amount':'Amount', 'unit':'Unit', 'ingredient':'Ingredient'}
		new_direction=''
	
	else: # Otherwise, the old recipe is pulled, and the ingredients and directions are parsed into temporary lists.
		new_recipe = request.session['new_recipe']
		recipe = Recipe(id=new_recipe)
		errors.append('old recipe #%s loaded' % new_recipe)
		for k,v in request.POST.iteritems():
			errors.append('%s = %s' %(k,v))
		for k,v in request.GET.iteritems():
			errors.append('%s = %s' %(k,v))
		
		# Check to see if form is filled out correctly, and then update recipe
		if request.method == 'POST':
			if 'finish' in request.POST:
				if 'recipe_name' in request.POST:
					recipe_name = request.POST['recipe_name']
					if not recipe_name or recipe_name == 'Recipe Name':
						errors.append("Come on man, you forgot the recipe name.")
					else:
						recipe.recipe_name = recipe_name
						recipe.save()
			if 'ingredient' in request.POST:
				if 'ingredient_amount' in request.POST:
					ingredient_amount = request.POST['ingredient_amount']
					if not ingredient_amount or ingredient_amount == 'Amount':
						errors.append('Dude you forgot an amount!')
						new_ingredient['amount'] = 'Amount'
						amount = False
					else:
						new_ingredient['amount'] = request.POST['ingredient_amount']
						amount = True
				if 'ingredient_unit' in request.POST:
					ingredient_unit = request.POST['ingredient_unit']
					if not ingredient_unit or ingredient_unit == 'Unit':
						errors.append('Where are the units?!')
						new_ingredient['unit'] = 'Unit'
						unit = False
					else:
						new_ingredient['unit'] = request.POST['ingredient_unit']
						unit = True
				if 'ingredient_type' in request.POST:
					ingredient_type = request.POST['ingredient_type']
					if not ingredient_type or ingredient_type == 'Ingredient':
						errors.append("Yo what's the ingredient dummy?")
						new_ingredient['ingredient'] = 'Ingredient'
						ingredient = False
					else:
						new_ingredient['ingredient'] = request.POST['ingredient_type']
						ingredient = True
				if ingredient and unit and amount:
					recipe.ingredients.item_name, recipe.ingredients.unit, recipe.ingredients.amount = \
					new_ingredient['ingredient'], new_ingredient['unit'], new_ingredient['amount']
					recipe.save()

		# If there are no errors, add the ingredients and/or directions
		if not errors:
			pass
		
	# Update the form
	recipe_name = recipe.recipe_name
	errors.append('recipe_name set to %s' % recipe_name)
	ingredient_list = recipe.ingredients.all()
	direction_list = recipe.directions.all()
	ingredients = [ingredient.__unicode__ for ingredient in ingredient_list]
	directions = [direction.step for direction in direction_list]
	step_number = len(directions) + 1
	errors.append(ingredient_list)
	
	return render(request, 'create_recipe.html', {'recipe_name': recipe_name, 'errors' : errors, 'ingredients': ingredients, 'new_ingredient': new_ingredient, 'directions': directions, 'new_direction':new_direction, 'step_number': step_number})
