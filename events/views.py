from django.shortcuts import render

def event_list(request):
    return render(request, 'events/event_list.html')

def event_detail(request, event_id):
    return render(request, 'events/event_detail.html', {'event_id': event_id})

def event_form(request):
    return render(request, 'events/event_form.html')
