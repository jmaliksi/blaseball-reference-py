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


def plate_appearances(batter_id=None):
    """Get the number of plate appearances for each historical batter. If batterId is specified, only that batter is returned.

    Returns dictionary {batter_id: count}"""
    params = {}
    if batter_id:
        params['batterId'] = batter_id

    response = requests.get(construct_url('plateAppearances'), params=params)
    response.raise_for_status()
    return {
        batter['batter_id']: batter['count'] for batter in response.json()['results']
    }


def at_bats(batter_id=None):
    """Get the number of at-bats for each historical batter. If batterId is specified, only that batter is returned.

    Returns dictionary {batter_id: count}"""
    params = {}
    if batter_id:
        params['batterId'] = batter_id

    response = requests.get(construct_url('atBats'), params=params)
    response.raise_for_status()
    return {
        batter['batter_id']: batter['count'] for batter in response.json()['results']
    }


def hits(batter_id=None):
    """Get the number of hits for each historical batter. If batterId is specified, only that batter is returned.

    Returns dictionary {batter_id: count}"""
    params = {}
    if batter_id:
        params['batterId'] = batter_id

    response = requests.get(construct_url('hits'), params=params)
    response.raise_for_status()
    return {
        batter['batter_id']: batter['count'] for batter in response.json()['results']
    }


def times_on_base(batter_id=None):
    """Get the number of times each historical batter got on base. If batterId is specified, only that batter is returned.

    Returns dictionary {batter_id: count}"""
    params = {}
    if batter_id:
        params['batterId'] = batter_id

    response = requests.get(construct_url('timesOnBase'), params=params)
    response.raise_for_status()
    return {
        batter['batter_id']: batter['count'] for batter in response.json()['results']
    }


def batting_average(batter_id=None):
    """Get the batting average (BA) for each historical batter. If batterId is specified, only that batter is returned.

    Returns dictionary {batter_id: avg}"""
    params = {}
    if batter_id:
        params['batterId'] = batter_id

    response = requests.get(construct_url('battingAverage'), params=params)
    response.raise_for_status()
    return {
        batter['id']: batter['value'] for batter in response.json()['results']
    }


def on_base_percentage(batter_id=None):
    """Get the on-base percentage (OBP) for each historical batter. If batterId is specified, only that batter is returned.

    Returns dictionary {batter_id: percent}"""
    params = {}
    if batter_id:
        params['batterId'] = batter_id

    response = requests.get(construct_url('onBasePercentage'), params=params)
    response.raise_for_status()
    return {
        batter['id']: batter['value'] for batter in response.json()['results']
    }


def on_base_plus_slugging(batter_id=None):
    """Get on-base percentage plus slugging (OPS) for each historical batter. If batterId is specified, only that batter is returned.

    Returns dictionary {batter_id: ops}"""
    params = {}
    if batter_id:
        params['batterId'] = batter_id

    response = requests.get(construct_url('OnBasePlusSlugging'), params=params)
    response.raise_for_status()
    return {
        batter['id']: batter['value'] for batter in response.json()['results']
    }


def slugging(batter_id=None):
    """Get the slugging percentage (SLG) for each historical batter. If batterId is specified, only that batter is returned.

    Returns dictionary {batter_id: percent}"""
    params = {}
    if batter_id:
        params['batterId'] = batter_id

    response = requests.get(construct_url('slugging'), params=params)
    response.raise_for_status()
    return {
        batter['id']: batter['value'] for batter in response.json()['results']
    }


def outs_recorded(pitcher_id=None):
    """Get the number of outs recorded by each historical pitcher. If pitcherId is specified, only that pitcher is returned.

    Returns dictionary {pitcher_id: count}"""
    params = {}
    if pitcher_id:
        params['pitcherId'] = pitcher_id

    response = requests.get(construct_url('outsRecorded'), params=params)
    response.raise_for_status()
    return {
        pitcher['pitcher_id']: pitcher['count'] for pitcher in response.json()['results']
    }


def hits_recorded(pitcher_id=None):
    """Get the number of hits recorded by each historical pitcher. If pitcherId is specified, only that pitcher is returned.

    Returns dictionary {pitcher_id: count}"""
    params = {}
    if pitcher_id:
        params['pitcherId'] = pitcher_id

    response = requests.get(construct_url('hitsRecorded'), params=params)
    response.raise_for_status()
    return {
        pitcher['pitcher_id']: pitcher['count'] for pitcher in response.json()['results']
    }


def walks_recorded(pitcher_id=None):
    """Get the number of walks recorded by each historical pitcher. If pitcherId is specified, only that pitcher is returned.

    Returns dictionary {pitcher_id: count}"""
    params = {}
    if pitcher_id:
        params['pitcherId'] = pitcher_id

    response = requests.get(construct_url('walksRecorded'), params=params)
    response.raise_for_status()
    return {
        pitcher['pitcher_id']: pitcher['count'] for pitcher in response.json()['results']
    }


def earned_runs(pitcher_id=None):
    """Get the number of runs earned by each historical pitcher. If pitcherId is specified, only that pitcher is returned.

    Returns dictionary {pitcher_id: count}"""
    params = {}
    if pitcher_id:
        params['pitcherId'] = pitcher_id

    response = requests.get(construct_url('earnedRuns'), params=params)
    response.raise_for_status()
    return {
        pitcher['id']: pitcher['value'] for pitcher in response.json()['results']
    }


def whip(pitcher_id=None):
    """Get the number of walks and hits per inning pitched (WHIP) for each historical pitcher.
    If pitcherId is specified, only that pitcher is returned.


    Returns dictionary {pitcher_id: value}"""
    params = {}
    if pitcher_id:
        params['pitcherId'] = pitcher_id

    response = requests.get(construct_url('whip'), params=params)
    response.raise_for_status()
    return {
        pitcher['id']: pitcher['value'] for pitcher in response.json()['results']
    }


def era(pitcher_id=None):
    """Get the earned run average (ERA) for each historical pitcher.
    If pitcherId is specified, only that pitcher is returned.

    Returns dictionary {pitcher_id: value}"""
    params = {}
    if pitcher_id:
        params['pitcherId'] = pitcher_id

    response = requests.get(construct_url('era'), params=params)
    response.raise_for_status()
    return {
        pitcher['id']: pitcher['value'] for pitcher in response.json()['results']
    }
