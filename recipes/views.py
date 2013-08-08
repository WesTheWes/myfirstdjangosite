from django.shortcuts import render
from recipes.models import Recipe
# Create your views here.

def create_recipe(request):
	if request.method != 'POST':
		raise Http404('Only POSTs are allowed')
	if 'new_recipe' not in request.session:
		recipe = Recipe()
		recipe.save()
		new_recipe = recipe.id
		request.session['new_recipe'] = new_recipe
	else:
		new_recipe = request.session['new_recipe']
		recipe = Recipe(id=new_recipe)
		ingredients = new_recipe.ingredients.all()
		ingredient_list = []
		for i,listitem in enumerate(ingredients):
			new_list = [listitem.amount, listitem.unit.unit_type, listitem.item_name.item]
			ingredient_list.append(new_list)
		directions = new_recipe.directions.all()
		
	errors = []
	if 'recipe_name' in request.GET:
		recipe_name = request.GET['recipe_name']
		if not recipe_name:
			errors.append("Come on man, you forgot the recipe name.")
		else:
			pass
	return render(request, 'create_recipe.html', {'errors' : errors, 'ingredients': ingredients, 'directions': directions})