from django import forms


class NameFilterForm(forms.Form):
    recipe_name = forms.CharField(label='Filter on recipe name', required=False)
    ingredient_name = forms.CharField(label='Filter on ingredient name', required=False)


