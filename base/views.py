import operator
from elo import Rating, rate_1vs1

from django.http import JsonResponse

from rest_framework.decorators import action
from rest_framework import viewsets

from base.models import Player
from base.serializers import PlayerSerializer
from matches.models import Match


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    @action(detail=False, methods=['get'])
    def elo(self, request):
        players = {}
        start = 1000
        matches = Match.objects.order_by('created_at').all()

        for match in matches:
            winner = match.winner.id
            loser = match.loser.id

            if winner not in players:
                players[winner] = Rating(start)

            if loser not in players:
                players[loser] = Rating(start)

            new_winner, new_loser = rate_1vs1(players[winner], players[loser])
            players[winner] = new_winner
            players[loser] = new_loser

        sorted_players = sorted(
            players.items(), key=operator.itemgetter(1))
        sorted_players.reverse()
        sorted_players = [
            {'player': p, 'score': int(s)} for p, s in sorted_players]

        return JsonResponse(sorted_players, safe=False)
