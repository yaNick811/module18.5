from django.shortcuts import render

# Главная страница
def index(request):
    return render(request, 'third_task/index.html')

# Страница "Магазин"
def shop(request):
    items = [
        "Игра 1",
        "Игра 2",
        "Игра 3",
    ]
    return render(request, 'third_task/shop.html', {'items': items})

# Страница "Корзина"
def cart(request):
    return render(request, 'third_task/cart.html')