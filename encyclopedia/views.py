from django.shortcuts import render
from . import util
from django.urls import reverse
from django.http import HttpResponseRedirect



def index(request):
    if request.method == "POST":
        search = request.POST.get("q")
        if search:
            if util.get_entry(search) or any(search in s for s in util.list_entries()) :
                matching = [s for s in util.list_entries() if search in s]
                return HttpResponseRedirect(reverse("encyclopedia:article", args=[matching[0]]))
            else:
                return render(request, "encyclopedia/index.html", {
                    "entries": util.list_entries(),
                    "error": "Article not found"
                })
        else:
            return render(request, "encyclopedia/index.html", {
                "entries": util.list_entries()
            })
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def article(request, name):
    return render(request,"encyclopedia/article.html",{
        "entry" : util.get_entry(name),
        "name" : name
    }) 