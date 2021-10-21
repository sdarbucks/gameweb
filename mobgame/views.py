from django.shortcuts import render

def mobgame_index(request):
    return render(request, 'mobgame/mobgame_index.html')
