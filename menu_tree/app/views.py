from django.shortcuts import render
from .models import Menu

def index(request):
    """
    Рендерит главную страницу со всеми элементами меню.
    """
    all_menus = Menu.objects.all()
    context = {'menus': all_menus}
    return render(request, 'app/index.html', context)

def draw_menu(request, path):
    """
    Динамически рендерит меню на основе пути.
    """
    path_parts = path.split('/')
    if len(path_parts) == 0:
        raise ValueError('Путь не может быть пустым')
    
    menu_name = path_parts[0]
    menu_item = path_parts[-1]
    
    context = {'menu_name': menu_name, 'menu_item': menu_item}
    return render(request, 'app/index.html', context)
