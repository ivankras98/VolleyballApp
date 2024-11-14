from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Player
from .forms import PlayerForm

def player_list(request):
    search_query = request.GET.get('search', '')  # Поисковый запрос
    sort_by = request.GET.get('sort', 'name')  # Поле для сортировки, по умолчанию имя
    position = request.GET.get('position')  # Позиция для фильтрации

    # Получаем уникальные позиции из базы данных для фильтра
    unique_positions = Player.objects.values_list('position', flat=True).distinct()

    # Начальный запрос к базе данных
    players = Player.objects.all()

    # Фильтрация по позиции
    if position:
        players = players.filter(position=position)
        print (players)
        print (position)


    # Поиск по имени или биографии
    if search_query:
        players = players.filter(Q(name__icontains=search_query) | Q(biography__icontains=search_query))

    # Применение сортировки
    players = players.order_by(sort_by)

    context = {
        'players': players,
        'search_query': search_query,
        'sort_by': sort_by,
        'position': position,
        'unique_positions': unique_positions,
    }
    return render(request, 'players/player_list.html', context)

def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    return render(request, 'players/player_detail.html', {'player': player})

def add_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('player_list')  # Перенаправление на страницу со списком игроков
    else:
        form = PlayerForm()
    return render(request, 'players/add_player.html', {'form': form})

def delete_player(request, pk):
    # Удаление игрока
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        player.delete()
        return redirect('player_list')  # Перенаправление на страницу со списком игроков
    return render(request, 'players/player_confirm_delete.html', {'player': player})
