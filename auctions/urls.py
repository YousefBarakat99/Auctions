from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("create/", views.create, name="create"),
    path("listing/<int:listing_id>/", views.listing, name="listing"),
    path("add/<int:listing_id>/", views.add, name="add"),
    path("remove/<int:listing_id>/", views.remove, name="remove"),
    path("watchlist/", views.watchlist, name="watchlist"),
    path("bid/<int:listing_id>/", views.bid, name="bid"),
    path("comment/<int:listing_id>/", views.comment, name="comment"),
    path("close/<int:listing_id>/", views.close, name="close"),
    path("categories/", views.categories, name="categories"),
    path("category/<str:category>/", views.category, name="category"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
