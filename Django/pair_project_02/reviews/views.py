from django.shortcuts import render, redirect
from .models import Reviews
from .forms import ReviewForm

# Create your views here.


def main(request):
    return render(request, "reviews/main.html")


def index(request):
    reviews = Reviews.objects.all()
    context = {
        "reviews": reviews,
    }
    return render(request, "reviews/index.html", context)


def create(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect("reviews:index")
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
    }
    return render(request, "reviews/create.html", context=context)


def detail(request, pk):
    review = Reviews.objects.get(pk=pk)
    context = {
        "review": review,
    }
    return render(request, "reviews/detail.html", context)


def delete(request, pk):
    review = Reviews.objects.get(pk=pk)
    review.delete()
    return redirect("reviews:index")


def update(request, pk):
    review = Reviews.objects.get(pk=pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect("reviews:detail", review.pk)
    else:
        review_form = ReviewForm(instance=review)
    context = {
        "review_form": review_form,
        "review": review,
    }
    return render(request, "reviews/create.html", context)
