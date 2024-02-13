from django.shortcuts import render
from django.urls import reverse

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
        'тесто, г': 50,
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

def recipe(request, servings=1):

    # recipes = {
    #     DATA.get('omlet'): reverse('omlet'),
    # }
    # context = recipes.items()

    pages = {
        'Омлет': reverse('omlet'),
        'Паста': reverse('pasta'),
        'Бутер': reverse('buter')
    }

    # context и параметры render менять не нужно подробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }

    print(context)
    return render(request, 'calculator/index.html', context)
