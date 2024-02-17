from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
    'robin-gud': {
        'яйца, шт': 2,
        'лук, шт': 1,
        'тесто, г': 20,
    },
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def recipe(request, dish):
    ingredients = DATA.get(dish, {})

    if request.GET.get('servings') is not None:
        servings = request.GET.get('servings')
    else:
        servings = 1

    temp_dict = {}
    for name, value in ingredients.items():
        if (float(value) * int(servings)) % 1 == 0:
            value = int(float(value) * int(servings))
        else:
            value = float(value) * int(servings)
        temp_dict[name] = value

    context = {'recipe': temp_dict}
    return render(request, 'calculator/index.html', context)
