from django.shortcuts import render

error_ingredient_dict = {
    "ошибка": "такого блюда нет"
}

DATA = {
    'omelet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'butter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def ingredients_views(request, ingredient):
    servings = request.GET.get('servings')
    if servings is not None and DATA.get(ingredient):
        ingredient_data = DATA.get(ingredient, error_ingredient_dict)
        ingredient_servings = {k: round(value * float(servings), 1) for k, value in ingredient_data.items()}
        context = {'recipe': ingredient_servings,
                   'ingredient': ingredient}
        return render(request, "calculator/index.html", context)
    else:
        ingredient_data = DATA.get(ingredient, error_ingredient_dict)
        context = {'recipe': ingredient_data,
                   'ingredient': ingredient}
        return render(request, "calculator/index.html", context)
