from app.models import MenuItem
from django import template
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()

@register.inclusion_tag('app/menu.html')
def draw_menu(menu_name: str = None, menu_item: str = None):
    
    def get_menu_hierarchy(current_item: str = None, submenu: list = None):
        if current_item is None:
            menu = list(items.filter(parent=None))
        else:
            menu = list(items.filter(parent__name=current_item))
        
        try:
            parent_index = menu.index(submenu[0].parent)
            menu.insert(parent_index + 1, submenu)
        except (IndexError, TypeError):
            pass
        
        try:
            parent_name = items.get(name=current_item).parent.name
            return get_menu_hierarchy(parent_name, menu)
        except AttributeError:
            return get_menu_hierarchy(submenu=menu)
        except ObjectDoesNotExist:
            return menu

    items = MenuItem.objects.filter(menu__name=menu_name)
    
    if menu_name == menu_item:
        return {'menu': get_menu_hierarchy()}
    else:
        return {'menu': get_menu_hierarchy(menu_item)}
