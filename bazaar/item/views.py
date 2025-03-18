from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Item
from .new_listing import NewListing


def item_detail(request, pk):
    get_item = get_object_or_404(Item, pk=pk)
    current_item_related_items = Item.objects.filter(listing_category =  get_item.listing_category, listing_is_sold = False ).exclude(pk=pk)[0:4]
    return render(request, 'item_detail.html',{
        'current_item' : get_item,
        'current_item_related_items': current_item_related_items
    })
@login_required
def delete_item(request, pk):
    deleteitem = get_object_or_404(Item, pk=pk, listing_created_by=request.user)
    deleteitem.delete()

    return redirect('my-listings')

@login_required
def new_listing(request):
    if request.method == 'POST':
        newList = NewListing(request.POST, request.FILES)

        if newList.is_valid():
            newItem = newList.save(commit=False)
            newItem.listing_created_by = request.user
            newItem.save()

            return redirect('item-detail', pk=newItem.id)
    else:
        newItem = NewListing()

    return render(request, 'new_listing.html', {
        'newItem': newItem,
        'addnewitem':'Add new item'
    })

@login_required
def panel(request):
    myitems = Item.objects.filter(listing_created_by = request.user)

    return render(request, 'mypanel.html', {
        'myitems': myitems,
    })