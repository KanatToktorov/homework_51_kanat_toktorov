from django.shortcuts import render
from django.http import HttpResponseRedirect

from source.webapp.cat import Cat


def main(request):
    return render(request, 'index.html')

def cat_stats(request):
    cat = Cat()
    cat.name = request.POST.get('name')
    if request.method == "GET":
        cat_stat = {
            'name': cat.name,
            'age': cat.age,
            'happy': cat.happy,
            'satiety': cat.satiety,
        }
        return render(request, "cat_stats.html", cat_stat)

    else:
        cat_action = request.POST.get("action")
        if cat_action == 'feed':
            cat.happy += 5
            cat.satiety += 15
        elif cat_action == 'play':
            cat.happy += 15
            cat.satiety -= 10
        cat_stat = {
            'name': cat.name,
            'age': cat.age,
            'happy': cat.happy,
            'satiety': cat.satiety,
        }
        return render(request, "cat_stats.html", cat_stat)


