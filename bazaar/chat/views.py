from django.shortcuts import  redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Chat
from .validate import MessageValidate
from item.models import Item                      


@login_required
def chat_start(request, item_pk):
    # new_conversation
    item = get_object_or_404(Item, pk=item_pk)

 

    if item.listing_created_by == request.user:
        return redirect('my-listings')
    
    # chats = Chat.objects.filter(item=item).filter(members__in=[request.user.id])
    chats = Chat.objects.filter(listing=item).filter(community__in=[request.user.id])

    if chats:
        return redirect('description', pk=chats.first().id)

    if request.method == 'POST':
        # form
        validatedfrm = MessageValidate(request.POST)

        if validatedfrm.is_valid():
            chat = Chat.objects.create(listing=item)
            chat.community.add(request.user)
            chat.community.add(item.listing_created_by)
            chat.save()
            # conversation_message COMMUNICATION
            communication = validatedfrm.save(commit=False)
            communication.chat = chat
            communication.generated_by = request.user
            communication.save()

            return redirect('item-detail', pk=item_pk)
    else:
        validatedfrm = MessageValidate()
    
    return render(request, 'chatstart.html', {
        'validatedfrm': validatedfrm
    })
# inbox
@login_required
def chatbox(request):
    # chats:conversations
    chats = Chat.objects.filter(community__in=[request.user.id])

    return render(request, 'chatbox.html', {
        'chats': chats
    })

# detail
# @login_required
# def description(request, pk):
#     # chat conversation
#     chat = Chat.objects.filter(community__in=[request.user.id]).get(pk=pk)

#     if request.method == 'POST':
#         # form validatedfrm
        
#         validatedfrm = MessageValidate(request.POST)

#         if validatedfrm.is_valid():
#             # communication :conversation_message
#             communication = validatedfrm.save(commit=False)
#             communication.chat = chat
#             communication. generated_by = request.user
#             communication.save()
#             chat.save()

#             return redirect('detail.html', pk=pk)
#     else:
#         validatedfrm = MessageValidate()

#     return render(request, 'detail.html', {
#         'chat': chat,
#         'validatedfrm': validatedfrm
#     })
@login_required
def description(request, pk):
    # Get the chat conversation
    chat = get_object_or_404(Chat, community__in=[request.user.id], pk=pk)

    if request.method == 'POST':
        # Handle form submission
        validatedfrm = MessageValidate(request.POST)
        if validatedfrm.is_valid():
            # Save the communication message
            communication = validatedfrm.save(commit=False)
            communication.message = chat
            communication.generated_by = request.user  # Correct field assignment
            communication.save()

            # Redirect to the same view
            return redirect('description', pk=pk)
    else:
        validatedfrm = MessageValidate()

    # Render the chat detail page
    return render(request, 'description.html', {
        'chat': chat,
        'validatedfrm': validatedfrm
    })