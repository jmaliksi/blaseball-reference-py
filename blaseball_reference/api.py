"""API for api dot blaseball-reference dot com"""

import requests

from blaseball_reference.models.game_event import GameEvent

API_VERSION = 'v1'
BASE_URL = 'https://api.blaseball-reference.com'


def construct_url(endpoint):
    return f'{BASE_URL}/{API_VERSION}/{endpoint}'


def events(player_id=None, game_id=None, pitcher_id=None, batter_id=None):
    """Get the list of game events that match the query. One of playerId, gameId, pitcherId, batterId must be specified."""

    params = {}
    if player_id:
        params['playerId'] = player_id
    elif game_id:
        params['gameId'] = game_id
    elif pitcher_id:
        params['pitcherId'] = pitcher_id
    elif batter_id:
        params['batterId'] = batter_id
    else:
        raise ValueError('No ID specified!')

    response = requests.get(construct_url('events'), params=params)
    response.raise_for_status()
    game_events = [
        GameEvent(**event) for event in response.json()['results']
    ]
    return game_events
