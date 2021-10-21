from django.shortcuts import render

def congame_index(request):
    return render(request, 'congame/congame_index.html')
