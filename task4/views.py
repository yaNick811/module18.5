from django.shortcuts import render

# Главная страница
def index(request):
    return render(request, 'fourth_task/index.html')

def shop(request):
    games = [
        "Atomic Heart",
        "Cyberpunk 2077",
        "PayDay 2",
    ]
    return render(request, 'fourth_task/shop.html', {'games': games})

def cart(request):
    return render(request, 'fourth_task/cart.html')