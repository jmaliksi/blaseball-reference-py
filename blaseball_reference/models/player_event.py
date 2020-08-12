"""PlayerEvent model"""
import enum


class PlayerEventType(enum.Enum):
    INCINERATION = enum.auto()
    PEANUT_GOOD = enum.auto()
    PEANUT_BAD = enum.auto()


class PlayerEvent(object):

    def __init__(self, **kwargs):
        """
        id	number
        The unique ID of the player event record.
        game_event_id	number
        The ID of the game event during which that this player event occurred.
        player_id	string
        The ID of the player that was affected as specified by the Blaseball API.
        event_type	string
        The type of event that occurred. One of INCINERATION, PEANUT_GOOD, PEANUT_BAD.
        """
        self.id = kwargs.get('id')
        self.game_event_id = kwargs.get('game_event_id')
        self.player_id = kwargs.get('player_id')
        self.event_type = PlayerEventType[kwargs['event_type']] if kwargs.get('event_type') else None
