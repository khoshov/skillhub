from courses.models import Category


def menu(request):
    categories = Category.objects.filter(parent__isnull=True, is_active=True).order_by('sort_order')
    return {'categories': categories}
