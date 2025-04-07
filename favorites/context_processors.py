from .favorites import Favorites

def favorites(request):
    favorites = Favorites(request)
    return {'favorites': favorites}