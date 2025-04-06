from django.shortcuts import render


# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Item
from .forms import ItemForm


def item_list(request):
    items = Item.objects.all()
    return render(request, 'crud1/item_list.html', {'items': items})


def item_create(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return JsonResponse({"id": item.id, "name": item.name, "description": item.description})
    return JsonResponse({"error": "Invalid data"}, status=400)


def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            return JsonResponse({"id": item.id, "name": item.name, "description": item.description})
    return JsonResponse({"message": "Item Edited"})


def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return JsonResponse({"message": "Item deleted"})