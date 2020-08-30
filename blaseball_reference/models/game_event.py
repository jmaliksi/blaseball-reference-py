"""GameEvent Model"""
import enum
from blaseball_reference.models.base_runner import BaseRunner
from blaseball_reference.models.player_event import PlayerEvent


class EventType(enum.Enum):
    UNKNOWN = enum.auto()
    NONE = enum.auto()
    OUT = enum.auto()
    STRIKEOUT = enum.auto()
    STOLEN_BASE = enum.auto()
    CAUGHT_STEALING = enum.auto()
    PICKOFF = enum.auto()
    WILD_PITCH = enum.auto()
    BALK = enum.auto()
    OTHER_ADVANCE = enum.auto()
    WALK = enum.auto()
    INTENTIONAL_WALK = enum.auto()
    HIT_BY_PITCH = enum.auto()
    FIELDERS_CHOICE = enum.auto()
    SINGLE = enum.auto()
    DOUBLE = enum.auto()
    TRIPLE = enum.auto()
    HOME_RUN = enum.auto()


class BattedBallType(enum.Enum):
    FLY_BALL = 'F'
    GROUND_BALL = 'G'
    LINE_DRIVE = 'L'
    POP_UP = 'P'

    @classmethod
    def from_key(cls, key):
        return {
            'F': cls.FLY_BALL,
            'G': cls.GROUND_BALL,
            'L': cls.LINE_DRIVE,
            'P': cls.POP_UP,
        }.get(key, None)


class PitchType(enum.Enum):
    CALLED_STRIKE = 'C'
    SWINGING_STRIKE = 'S'
    BALL = 'B'
    FOUL = 'F'
    PICKOFF_FIRST = '1'
    PICKOFF_SECOND = '2'
    PICKOFF_THIRD = '3'
    PICKOFF_FOURTH = '4'
    CATCHER_PICKOFF_FIRST = '+1'
    CATCHER_PICKOFF_SECOND = '+2'
    CATCHER_PICKOFF_THIRD = '+3'
    CATCHER_PICKOFF_FOURTH = '+4'
    FOUL_BUNT = 'L'
    MISSED_BUNT = 'M'
    SWINGING_STRIKE_ON_PITCHOUT = 'Q'
    FOUL_BALL_ON_PITCHOUT = 'R'
    INTENTIONAL_BALL = 'I'
    PITCHOUT = 'P'
    HIT_BY_PITCH = 'H'
    UNKNOWN_STRIKE = 'K'
    UNKNOWN_OR_MISSING = 'U'
    HIT = 'X'

    @classmethod
    def from_key(cls, key):
        for e in cls:
            if e.value == key:
                return e
        return None


class GameEvent(object):
    """
    Represents an event in a Blaseball game.
    https://api.blaseball-reference.com/docs

    """

    def __init__(self, **kwargs):
        """
        id	number
        The unique ID of the game event record.
        game_id	string
        The ID of the game record as specified by the Blaseball API.
        event_type	string
        The type of event that occurred. One of UNKNOWN, NONE, OUT, STRIKEOUT, STOLEN_BASE, CAUGHT_STEALING, PICKOFF, WILD_PITCH, BALK, OTHER_ADVANCE, WALK, INTENTIONAL_WALK, HIT_BY_PITCH, FIELDERS_CHOICE, SINGLE, DOUBLE, TRIPLE, HOME_RUN.

        event_index	number
        The position of this event relative to the other events in the game (0-indexed).

        inning	number
        The inning in which the event occurred (1-indexed).

        top_of_inning	boolean
        Did this event take place in the top or the bottom of the inning?
        outs_before_play	number
        The number of outs before this event took place.
        batter_id	string
        The ID of the pitcher's team record as specified by the Blaseball API.

        batter_team_id	string
        The ID of the batter's team record as specified by the Blaseball API.

        pitcher_id	string
        The ID of the pitcher's player record as specified by the Blaseball API.

        home_score	number
        The score of the home team.
        away_score	number
        The score of the away team.
        home_strike_count	number
        The number of strikes required to strike out a batter on the home team.
        away_strike_count	number
        The number of strikes required to strike out a batter on the away team.
        batter_count	number
        The total number of batters that have taken the plate in this game.
        pitches	string
        The pitches in this play. See Retrosheet's MEVENT for symbology.

        total_strikes	number
        The total number of strikes that occurred in the play.
        total_balls	number
        The total number of balls that occurred in the play.
        total_fouls	number
        The total number of foul balls that occurred in the play (not currently trackable).

        is_leadoff	boolean
        Is this batter leading off the inning?
        is_pinch_hit	boolean
        Is this batter pinch hitting?
        lineup_position	number
        Not currently implemented.
        is_last_event_for_plate_appearance	boolean
        Is this the last event in the plate appearance? (Almost always true; false if a base is stolen, for example).

        bases_hit	number
        The number of bases reached in the hit.
        runs_batted_in	number
        The number of runs batted in.
        is_sacrifice_hit	boolean
        Was this a sacrifice hit?
        is_sacrifice_fly	boolean
        Was this a sacrifice fly?
        outs_on_play	number
        The number of outs that occurred from this play.
        is_double_play	boolean
        Is this a double play?
        is_triple_play	boolean
        Is this a triple play?
        is_wild_pitch	boolean
        Was this event a wild pitch?
        batted_ball_type	string
        F - fly ball, G - ground ball, L - line drive, P - pop-up.

        is_bunt	boolean
        Was this play a bunt?
        errors_on_play	number
        The number of errors that occurred on the play.
        batter_base_after_play	number
        The number of batters on base after the play.
        is_last_game_event	boolean
        Is this the last event in the game?
        event_text	string
        The message text descriptions that contributed to this event.
        additional_context	string
        Additional comments.

        base_runners list(BaseRunner)
        player_events list(PlayerEvent)
        """
        self.id = kwargs.get('id')
        self.game_id = kwargs.get('game_id')
        self.event_type = EventType[kwargs.get('event_type', 'UNKNOWN')]
        self.event_index = kwargs.get('event_index')
        self.inning = kwargs.get('inning')
        self.top_of_inning = kwargs.get('top_of_inning')
        self.outs_before_play = kwargs.get('outs_before_play')
        self.batter_id = kwargs.get('batter_id')
        self.batter_team_id = kwargs.get('batter_team_id')
        self.pitcher_id = kwargs.get('pitcher_id')
        self.pitcher_team_id = kwargs.get('pitcher_team_id')
        self.home_score = int(kwargs.get('home_score', '0'))
        self.away_score = int(kwargs.get('away_score', '0'))
        self.home_strike_count = kwargs.get('home_strike_count')
        self.away_strike_count = kwargs.get('away_strike_count')
        self.batter_count = kwargs.get('batter_count')
        self.pitches = [PitchType.from_key(p) for p in kwargs.get('pitches', [])]  # array
        self.total_strikes = kwargs.get('total_strikes')
        self.total_balls = kwargs.get('total_balls')
        self.total_fouls = kwargs.get('total_fouls')
        self.is_leadoff = kwargs.get('is_leadoff')
        self.is_pinch_hit = kwargs.get('is_pinch_hit')
        self.lineup_position = kwargs.get('lineup_position')
        self.is_last_event_for_plate_appearance = kwargs.get('is_last_event_for_plate_appearance')
        self.bases_hit = kwargs.get('bases_hit')
        self.runs_batted_in = kwargs.get('runs_batted_in')
        self.is_sacrifice_hit = kwargs.get('is_sacrifice_hit')
        self.is_sacrifice_fly = kwargs.get('is_sacrifice_fly')
        self.outs_on_play = kwargs.get('outs_on_play')
        self.is_double_play = kwargs.get('is_double_play')
        self.is_triple_play = kwargs.get('is_triple_play')
        self.is_wild_pitch = kwargs.get('is_wild_pitch')
        self.batted_ball_type = BattedBallType.from_key(kwargs.get('batted_ball_type'))
        self.is_bunt = kwargs.get('is_bunt')
        self.errors_on_play = kwargs.get('errors_on_play')
        self.batter_base_after_play = kwargs.get('batter_base_after_play')
        self.is_last_game_event = kwargs.get('is_last_game_event')
        self.event_text = kwargs.get('event_text')  # array
        self.additional_context = kwargs.get('additional_context')

        self.base_runners = [
            BaseRunner(**base_runner) for base_runner in kwargs.get('base_runners', [])
        ]
        self.player_events = [
            PlayerEvent(**player_event) for player_event in kwargs.get('player_events', [])
        ]
