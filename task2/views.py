from django.shortcuts import render
from django.views import View

# Функциональное представление
def function_based_view(request):
    return render(request, 'second_task/function_based_view.html')

# Классовое представление
class ClassBasedView(View):
    def get(self, request):
        return render(request, 'second_task/class_based_view.html')