from django.shortcuts import render
from .forms import UserRegisterForm

# Псевдо-список существующих пользователей
users = ["admin", "user1", "user2"]

# Представление с использованием Django формы
def sign_up_by_django(request):
    info = {}
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            repeat_password = form.cleaned_data["repeat_password"]
            age = form.cleaned_data["age"]

            # Проверки
            if password != repeat_password:
                info["error"] = "Пароли не совпадают"
            elif age < 18:
                info["error"] = "Вы должны быть старше 18"
            elif username in users:  # Проверка на существование пользователя
                info["error"] = "Пользователь уже существует"
            else:
                # Добавляем нового пользователя в список
                users.append(username)
                return render(request, "fifth_task/success.html", {"username": username})
    else:
        form = UserRegisterForm()

    info["form"] = form
    return render(request, "fifth_task/registration_page.html", info)

# Представление с использованием HTML формы
def sign_up_by_html(request):
    info = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = int(request.POST.get("age"))

        # Проверки
        if password != repeat_password:
            info["error"] = "Пароли не совпадают"
        elif age < 18:
            info["error"] = "Вы должны быть старше 18"
        elif username in users:  # Проверка на существование пользователя
            info["error"] = "Пользователь уже существует"
        else:
            # Добавляем нового пользователя в список
            users.append(username)
            return render(request, "fifth_task/success.html", {"username": username})

    return render(request, "fifth_task/registration_page.html", info)