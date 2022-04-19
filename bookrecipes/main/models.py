from django.db import models


class Ingredient(models.Model):
    """Ingredient"""

    name = models.CharField("Name", max_length=250, unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"


class Recipe(models.Model):
    """Recipe"""

    name = models.CharField("Name", max_length=250, unique=True)
    ingredients = models.ManyToManyField(
        "Ingredient", verbose_name="Ingredients", related_name="ingredient_recipe"
    )

    description = models.TextField('Description')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"






