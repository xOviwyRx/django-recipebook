from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Recipe
from .forms import NameFilterForm


def index(request):
    """Main page. Redirect on `/recipes`"""
    response = redirect(reverse("recipes"))
    return response


def recipes(request):
    """Recipe list with search by name and ingredient"""
    recipes_objects = Recipe.objects.all()
    form_search = NameFilterForm(request.GET)
    if form_search.is_valid():
        if form_search.cleaned_data["recipe_name"]:
            recipes_objects = recipes_objects. \
                filter(name__icontains=form_search.cleaned_data["recipe_name"])
        if form_search.cleaned_data["ingredient_name"]:
            recipes_objects = recipes_objects. \
                filter(ingredients__name__icontains=form_search.cleaned_data["ingredient_name"])
    return render(
        request,
        "main/index.html",
        {
            "recipes": recipes_objects,
            "form": {
                "description": "Here you can see recipe list",
            },
            "form_search": form_search,
        },
    )
