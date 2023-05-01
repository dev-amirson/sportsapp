from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Team, Player
from .forms import TeamForm, PlayerForm, CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def home(request):
    return render(request, 'home.html')

@login_required
def team_list(request):
    teams = Team.objects.all()
    return render(request, 'team_list.html', {'teams': teams})

@login_required
def team_detail(request, pk):
    team = get_object_or_404(Team, pk=pk)
    return render(request, 'team_detail.html', {'team': team})

@login_required
def team_create(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save()
            return redirect('team_detail', pk=team.pk)
    else:
        form = TeamForm()
    return render(request, 'team_create.html', {'form': form})

@login_required
def team_update(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        form = TeamForm(request.POST, instance=team)
        if form.is_valid():
            team = form.save()
            return redirect('team_detail', pk=team.pk)
    else:
        form = TeamForm(instance=team)
    return render(request, 'team_update.html', {'form': form})

@login_required
def team_delete(request, pk):
    team = get_object_or_404(Team, pk=pk)
    team.delete()
    return redirect('team_list')

@login_required
def player_list(request):
    players = Player.objects.all()
    return render(request, 'player_list.html', {'players': players})

@login_required
def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'player_detail.html', {'player': player})

@login_required
def player_create(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save()
            return redirect('player_detail', pk=player.pk)
    else:
        form = PlayerForm()
    return render(request, 'player_create.html', {'form': form})

@login_required
def player_update(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            player = form.save()
            return redirect('player_detail', pk=player.pk)
    else:
        form = PlayerForm(instance=player)
    return render(request, 'player_update.html', {'form': form})

@login_required
def player_delete(request, pk):
    player = get_object_or_404(Player, pk=pk)
    player.delete()
    return redirect('player_list')

@login_required
def assign_players_to_team(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.method == 'POST':
        player_ids = request.POST.getlist('players')
        players = Player.objects.filter(id__in=player_ids)

        for player in players:
            team.player_set.add(player.id)

        return redirect('team_detail', pk=team_id)
    else:
        players = Player.objects.exclude(teams=team)
        return render(request, 'assign_players_to_team.html', {'team': team, 'players': players})