from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Recipe, Ingredient
from .forms import NameFilterForm


def index(request):
    """Main page. Redirect on `/recipes`"""
    response = redirect(reverse("recipes"))
    return response


def recipes(request):
    """Recipe list with search by name and ingredient"""
    recipes_objects = Recipe.objects.all()
    if len(recipes_objects):
        # form_search = NameFilterForm(request.GET)
        # if form_search.is_valid():
        #     if form_search.cleaned_data["recipe_name"]:
        #         recipes_objects = recipes_objects. \
        #             filter(name__icontains=form_search.cleaned_data["recipe_name"])
        #     if form_search.cleaned_data["ingredient_name"]:
        #         recipes_objects = recipes_objects. \
        #             filter(ingredients__name__icontains=form_search.cleaned_data["ingredient_name"])
        # return render(
        #     request,
        #     "main/index.html",
        #     {
        #         "recipes": recipes_objects,
        #         "form": {
        #             "description": "Here you can see recipe list",
        #         },
        #         "form_search": form_search
        #     },
        # )
        try:
            recipe_id = int(request.GET.get("recipe_id"))
        except (ValueError, TypeError):
            recipe_id = None

        try:
            recipe_ingredient_id = int(request.GET.get("ingredient_id"))
        except (ValueError, TypeError):
            recipe_ingredient_id = None

        query = Q()
        if recipe_id:
            query.add(
                Q(pk=recipe_id), Q.AND,
            )
        if recipe_ingredient_id:
            query.add(
                Q(ingredients__pk=recipe_ingredient_id), Q.AND,
            )
        recipes_objects = Recipe.objects.prefetch_related("ingredients").filter(query)
        ingredients_lookup = Ingredient.objects.all()
        recipes_lookup = Recipe.objects.all()

        return render(
            request,
            "main/index.html",
            {
                "recipes": recipes_objects,
                "form": {
                    "description": "Here you can see recipe list",
                    "ingredient": {
                        "title": "Ingredient",
                        "objects": ingredients_lookup,
                        "selected": recipe_ingredient_id,
                    },
                    "recipe": {
                        "title": "Recipe",
                        "objects": recipes_lookup,
                        "selected": recipe_id,
                    },
                },
            },
        )
    else:
        """No any recipe - show base.html template"""
        return render(
            request, "base.html"
        )

