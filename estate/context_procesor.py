from root.models import Category

def jeneral(request):
    categorys = Category.objects.all()
    context = {
        'categorys':categorys
    }
    return context