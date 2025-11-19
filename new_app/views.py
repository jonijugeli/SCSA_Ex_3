from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Item

def hello_veiw(request):
    return render(request, 'new_app/hello.html')

def about_view(request):
    return render(request, 'new_app/about.html')

def item_detail_view(request, item_id):

    try:
        item = Item.objects.get(id = item_id)
        
        return HttpResponse(f"მოცემული აიტემის აიდია: {item_id}")
    except:
        raise Http404("ამისთანა არაფერი არაა სმნ")