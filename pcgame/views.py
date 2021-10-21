from django.shortcuts import render

def pcgame_index(request):
    return render(request, 'pcgame/pcgame_index.html')
