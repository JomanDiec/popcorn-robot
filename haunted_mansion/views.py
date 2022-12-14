from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from haunted_mansion.models import *

# Create your views here.
def index(request):
    return HttpResponse('test')

def haunted_mansion(request):

    game_state = GameState.objects.get(id=1)
    new_game = game_state.new_game
    health = game_state.health
    bedroom_key = game_state.bedroom_key
    front_key = game_state.front_key
    jack_found = game_state.jack_found

    context = {'new_game' : new_game, 'health' : health, 'bedroom_key' : bedroom_key, 'front_key' : front_key, 'jack_found' : jack_found}
    return render(request,'ajax_haunted_mansion.html', context)