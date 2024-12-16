from .models import Category

def menu_links(request):
    links = Category.object.all()

    return dict(links=links)