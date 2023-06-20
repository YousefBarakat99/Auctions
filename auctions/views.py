from hmac import new
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, auctions, bid, comments


def index(request):
    return render(request, "auctions/index.html", {
        "listings": auctions.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

class NewListingForm(forms.ModelForm):
    class Meta:
        model = auctions  
        fields = ['title', 'description', 'bid', 'category', 'image']



def create(request):
    if request.method == "POST":
        form = NewListingForm(request.POST)
        if form.is_valid():
            new_listing = form.save(commit=False)
            new_listing.user = request.user
            new_listing.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/create.html", {
                "form": form
            })
    else:
        return render(request, "auctions/create.html", {
            "form": NewListingForm()
        })
    
def listing(request, listing_id):
    listing = auctions.objects.get(pk=listing_id)
    bids = listing.bids.all()
    bid_count = bids.count()
    if bid_count == 0:
        highest_bid = None
        highest_bidder = None
    else:
        highest_bid_obj = bids.order_by('-bid')[0]
        highest_bid = highest_bid_obj.bid
        highest_bidder = highest_bid_obj.user
    return render(request, "auctions/listing.html", {
        "listing": listing,
        "comments": listing.comments.all(),
        "bids": bids,
        "user": request.user,
        "watchlist": request.user in listing.watchlist.all(),
        "highest_bid": highest_bid,
        "highest_bidder": highest_bidder,
    })




def remove(request, listing_id):
    listing = auctions.objects.get(pk=listing_id)
    listing.watchlist.remove(request.user)
    listing.save()
    return HttpResponseRedirect(reverse("listing", args=(listing_id,)))

def add(request, listing_id):
    listing = auctions.objects.get(pk=listing_id)
    listing.watchlist.add(request.user)
    listing.save()
    return HttpResponseRedirect(reverse("listing", args=(listing_id,)))

def watchlist(request):
    return render(request, "auctions/watchlist.html", {
        "listings": User.objects.get(pk=request.user.id).watchlist.all()
    })

class NewBidForm(forms.ModelForm):
    class Meta:
        model = bid
        fields = ['bid']

def bid(request, listing_id):
    if request.method == "POST":
        form = NewBidForm(request.POST)
        if form.is_valid():
            new_bid = form.save(commit=False)
            new_bid.user = request.user
            new_bid.auction = auctions.objects.get(pk=listing_id)
            new_bid.save()
            new_bid.auction.bid = new_bid.bid
            new_bid.auction.save()
            return HttpResponseRedirect(reverse("listing", args=(listing_id, )))
        else:
            return render(request, "auctions/listing.html", {
                "form": form,
                "message": "Invalid bid. Bid must be higher than current bid."
            })
    else:
        return render(request, "auctions/listing.html", {
            "form": NewBidForm()
        })


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = comments
        fields = ['comment']

def comment(request, listing_id):
    if request.method == "POST":
        form = NewCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.auction = auctions.objects.get(pk=listing_id)
            new_comment.save()
            new_comment.auction.comments.add(new_comment)
            return HttpResponseRedirect(reverse("listing", args=(listing_id, )))
        else:
            return render(request, "auctions/listing.html", {
                "form": form
            })
    else:
        return render(request, "auctions/listing.html", {
            "form": NewCommentForm()
        })
    
def close(request, listing_id):
    listing = auctions.objects.get(pk=listing_id)
    listing.active = False
    listing.save()
    return HttpResponseRedirect(reverse("listing", args=(listing_id, )))

def categories(request):
    return render(request, "auctions/categories.html", {
        "categories": auctions.objects.values('category').distinct()
    })

def category(request, category):
    return render(request, "auctions/category.html", {
        "listings": auctions.objects.filter(category=category),
        "category": category,
    })

