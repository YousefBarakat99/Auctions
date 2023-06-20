from django.contrib import admin
from .models import User, auctions, bid, comments

class Watchlist(admin.ModelAdmin):
    filter_horizontal = ("watchlist",)

# Register your models here.
admin.site.register(User, Watchlist)
admin.site.register(auctions)
admin.site.register(bid)
admin.site.register(comments)