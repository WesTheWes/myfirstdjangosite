from django.shortcuts import render

# Create your views here.

def create_recipe(request):
	errors = []
	ingredients = []
	directions = []
	if 'recipe_name' in request.GET:
		recipe_name = request.GET['recipe_name']
		if not recipe_name:
			errors.append("Come on man, you forgot the recipe name.")
		else:
			pass
	return render(request, 'create_recipe.html', {'errors' : errors, 'ingredients': ingredients, 'directions': directions})