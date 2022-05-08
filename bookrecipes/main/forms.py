from django import forms


class NameFilterForm(forms.Form):
    recipe_name = forms.CharField(label='Recipe', required=False)
    ingredient_name = forms.CharField(label='Ingredient', required=False)


