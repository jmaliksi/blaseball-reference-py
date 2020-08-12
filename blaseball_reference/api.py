"""API for api dot blaseball-reference dot com"""

import requests

from blaseball_reference.models.game_event import GameEvent, EventType

API_VERSION = 'v1'
BASE_URL = 'https://api.blaseball-reference.com'


def construct_url(endpoint):
    return f'{BASE_URL}/{API_VERSION}/{endpoint}'


def prepare_id(id_):
    """if id_ is string uuid, return as is, if list, format as comma separated list."""
    if isinstance(id_, list):
        return ','.join(id_)
    elif isinstance(id_, str):
        return id_
    else:
        raise ValueError(f'Incorrect ID type: {type(id_)}')


def raw_events(**kwargs):
    """
    Download all of the game events, base runners, and player events. Child data (base runners, player events) are
provided as their own lists and are not mapped into their parents, and thus must be matched by game_event_id.

    This can cause a pretty hefty toll on the datablase, so use with caution. If you're absolutely sure, to prove
    that you've read this, set the keyword argument `are_you_sure` to True.
    """
    if not kwargs.get('are_you_sure'):
        raise Exception('Please mind the datablase.')
    response = requests.get(construct_url('data/events'))
    response.raise_for_status()
    # I'm not going to try to format a raw data dump. This is on you.
    return response.json()


def events(player_id=None,
           game_id=None,
           pitcher_id=None,
           batter_id=None,
           player_events=False,
           base_runners=False,
           type_=None,
           sort_by=None,
           sort_direction=None):
    """Get the list of game events that match the query. One of playerId, gameId, pitcherId, batterId must be specified.

    Any ID may be a single string UUID or a list of string UUIDs.
    `player_events`: bool Include PlayerEvents in results.
    `base_runners`: bool Include BaseRunners in results.
    `sort_by`: str The field by which to sort. Most text and numeric columns are supported.
    `sort_direction`: str "asc" or "desc".
    `type_`: event by which to filter.

    Returns an iterator of `GameEvent` objects.
    """

    params = {
        'baseRunners': base_runners,
        'playerEvents': player_events,
    }
    if player_id:
        params['playerId'] = prepare_id(player_id)
    elif game_id:
        params['gameId'] = prepare_id(game_id)
    elif pitcher_id:
        params['pitcherId'] = prepare_id(pitcher_id)
    elif batter_id:
        params['batterId'] = prepare_id(batter_id)
    else:
        raise ValueError('No ID specified!')

    if isinstance(type_, GameEvent):
        type_ = type_.name
    if type_:
        params['type'] = type_

    response = requests.get(construct_url('events'), params=params)
    response.raise_for_status()
    results = response.json()['results']
    for game_event in results:
        yield GameEvent(**game_event)


def count_by_type(event_type, pitcher_id=None, batter_id=None):
    """Get the number of events for a batter or pitcher with a certain event_type.
    `event_type` can be of type `EventType` or a raw string.
    `pitcher_id` and `batter_id` are optional and can be a single string or list.
    Returns a dictionary of dictionaries with format:
    {
        'pitchers': {
            pitcher_id: count,
        },
        'batters': {
            batter_id: count,
        }
    }
    """
    if isinstance(event_type, EventType):
        event_type = event_type.name
    params = {
        'eventType': event_type,
    }
    if pitcher_id:
        params['pitcherId'] = prepare_id(pitcher_id)
    if batter_id:
        params['batterId'] = prepare_id(pitcher_id)

    response = requests.get(construct_url('countByType'), params=params)
    response.raise_for_status()
    res = response.json()
    return {
        'pitchers': {pitcher['pitcher_id']: pitcher['count'] for pitcher in res.get('pitchers', [])},
        'batters': {batter['batter_id']: batter['count'] for batter in res.get('batters', [])},
    }


def plate_appearances(batter_id=None):
    """Get the number of plate appearances for each historical batter. If batterId is specified, only that batter is returned.

    `batter_id` is a single string UUID or list of string UUIDs.
    Returns dictionary {batter_id: count}"""
    params = {}
    if batter_id:
        params['batterId'] = prepare_id(batter_id)

    response = requests.get(construct_url('plateAppearances'), params=params)
    response.raise_for_status()
    return {
        batter['batter_id']: batter['count'] for batter in response.json()['results']
    }


def at_bats(batter_id=None):
    """Get the number of at-bats for each historical batter. If batterId is specified, only that batter is returned.

    `batter_id` is a single string UUID or list of string UUIDs.
    Returns dictionary {batter_id: count}"""
    params = {}
    if batter_id:
        params['batterId'] = prepare_id(batter_id)

    response = requests.get(construct_url('atBats'), params=params)
    response.raise_for_status()
    return {
        batter['batter_id']: batter['count'] for batter in response.json()['results']
    }


def hits(batter_id=None):
    """Get the number of hits for each historical batter. If batterId is specified, only that batter is returned.

    `batter_id` is a single string UUID or list of string UUIDs.
    Returns dictionary {batter_id: count}"""
    params = {}
    if batter_id:
        params['batterId'] = prepare_id(batter_id)

    response = requests.get(construct_url('hits'), params=params)
    response.raise_for_status()
    return {
        batter['batter_id']: batter['count'] for batter in response.json()['results']
    }


def times_on_base(batter_id=None):
    """Get the number of times each historical batter got on base. If batterId is specified, only that batter is returned.

    `batter_id` is a single string UUID or list of string UUIDs.
    Returns dictionary {batter_id: count}"""
    params = {}
    if batter_id:
        params['batterId'] = prepare_id(batter_id)

    response = requests.get(construct_url('timesOnBase'), params=params)
    response.raise_for_status()
    return {
        batter['batter_id']: batter['count'] for batter in response.json()['results']
    }


def batting_average(batter_id=None):
    """Get the batting average (BA) for each historical batter. If batterId is specified, only that batter is returned.

    `batter_id` is a single string UUID or list of string UUIDs.
    Returns dictionary {batter_id: avg}"""
    params = {}
    if batter_id:
        params['batterId'] = prepare_id(batter_id)

    response = requests.get(construct_url('battingAverage'), params=params)
    response.raise_for_status()
    return {
        batter['id']: batter['value'] for batter in response.json()['results']
    }


def on_base_percentage(batter_id=None):
    """Get the on-base percentage (OBP) for each historical batter. If batterId is specified, only that batter is returned.

    `batter_id` is a single string UUID or list of string UUIDs.
    Returns dictionary {batter_id: percent}"""
    params = {}
    if batter_id:
        params['batterId'] = prepare_id(batter_id)

    response = requests.get(construct_url('onBasePercentage'), params=params)
    response.raise_for_status()
    return {
        batter['id']: batter['value'] for batter in response.json()['results']
    }


def on_base_plus_slugging(batter_id=None):
    """Get on-base percentage plus slugging (OPS) for each historical batter. If batterId is specified, only that batter is returned.

    `batter_id` is a single string UUID or list of string UUIDs.
    Returns dictionary {batter_id: ops}"""
    params = {}
    if batter_id:
        params['batterId'] = prepare_id(batter_id)

    response = requests.get(construct_url('OnBasePlusSlugging'), params=params)
    response.raise_for_status()
    return {
        batter['id']: batter['value'] for batter in response.json()['results']
    }


def slugging(batter_id=None):
    """Get the slugging percentage (SLG) for each historical batter. If batterId is specified, only that batter is returned.

    `batter_id` is a single string UUID or list of string UUIDs.
    Returns dictionary {batter_id: percent}"""
    params = {}
    if batter_id:
        params['batterId'] = prepare_id(batter_id)

    response = requests.get(construct_url('slugging'), params=params)
    response.raise_for_status()
    return {
        batter['id']: batter['value'] for batter in response.json()['results']
    }


def outs_recorded(pitcher_id=None):
    """Get the number of outs recorded by each historical pitcher. If pitcherId is specified, only that pitcher is returned.

    `batter_id` is a single string UUID or list of string UUIDs.
    Returns dictionary {pitcher_id: count}"""
    params = {}
    if pitcher_id:
        params['pitcherId'] = prepare_id(pitcher_id)

    response = requests.get(construct_url('outsRecorded'), params=params)
    response.raise_for_status()
    return {
        pitcher['pitcher_id']: pitcher['count'] for pitcher in response.json()['results']
    }


def hits_recorded(pitcher_id=None):
    """Get the number of hits recorded by each historical pitcher. If pitcherId is specified, only that pitcher is returned.

    `pitcher_id` is a single string UUID or list of string UUIDs.
    Returns dictionary {pitcher_id: count}"""
    params = {}
    if pitcher_id:
        params['pitcherId'] = prepare_id(pitcher_id)

    response = requests.get(construct_url('hitsRecorded'), params=params)
    response.raise_for_status()
    return {
        pitcher['pitcher_id']: pitcher['count'] for pitcher in response.json()['results']
    }


def walks_recorded(pitcher_id=None):
    """Get the number of walks recorded by each historical pitcher. If pitcherId is specified, only that pitcher is returned.

    `pitcher_id` is a single string UUID or list of string UUIDs.
    Returns dictionary {pitcher_id: count}"""
    params = {}
    if pitcher_id:
        params['pitcherId'] = prepare_id(pitcher_id)

    response = requests.get(construct_url('walksRecorded'), params=params)
    response.raise_for_status()
    return {
        pitcher['pitcher_id']: pitcher['count'] for pitcher in response.json()['results']
    }


def earned_runs(pitcher_id=None):
    """Get the number of runs earned by each historical pitcher. If pitcherId is specified, only that pitcher is returned.

    `pitcher_id` is a single string UUID or list of string UUIDs.
    Returns dictionary {pitcher_id: count}"""
    params = {}
    if pitcher_id:
        params['pitcherId'] = prepare_id(pitcher_id)

    response = requests.get(construct_url('earnedRuns'), params=params)
    response.raise_for_status()
    return {
        pitcher['id']: pitcher['value'] for pitcher in response.json()['results']
    }


def whip(pitcher_id=None):
    """Get the number of walks and hits per inning pitched (WHIP) for each historical pitcher.
    If pitcherId is specified, only that pitcher is returned.

    `pitcher_id` is a single string UUID or list of string UUIDs.
    Returns dictionary {pitcher_id: value}"""
    params = {}
    if pitcher_id:
        params['pitcherId'] = prepare_id(pitcher_id)

    response = requests.get(construct_url('whip'), params=params)
    response.raise_for_status()
    return {
        pitcher['id']: pitcher['value'] for pitcher in response.json()['results']
    }


def era(pitcher_id=None):
    """Get the earned run average (ERA) for each historical pitcher.
    If pitcherId is specified, only that pitcher is returned.

    `pitcher_id` is a single string UUID or list of string UUIDs.
    Returns dictionary {pitcher_id: value}"""
    params = {}
    if pitcher_id:
        params['pitcherId'] = prepare_id(pitcher_id)

    response = requests.get(construct_url('era'), params=params)
    response.raise_for_status()
    return {
        pitcher['id']: pitcher['value'] for pitcher in response.json()['results']
    }
