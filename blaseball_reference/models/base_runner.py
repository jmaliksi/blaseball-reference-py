"""Base runner model."""

class BaseRunner(object):

    def __init__(self, **kwargs):
        """
        id	number
        The unique ID of the base runner record.
        game_event_id	number
        The ID of the game event to which this base runner record belongs.
        runner_id	string
        The ID of the base runner as specified by the Blaseball API.
        responsible_pitcher_id	string
        The ID of the pitcher that is responsible for this base runner, as specified by the Blaseball API.

        base_before_play	number
        The base that the base runner was on before the play started. 0 means the runner was not on base.
        base_after_play	number
        The base that the base runner was on after the play ended. 0 means the runner is no longer on base; 4 means the runner reached home.

        was_base_stolen	boolean
        Was a base stolen by this runner on the play?
        was_caught_stealing	boolean
        Was this runner caught stealing in the play?
        was_picked_off	boolean
        Was this runner picked off in the play?
        """
        self.id = kwargs.get('id')
        self.game_event_id = kwargs.get('game_event_id')
        self.runner_id = kwargs.get('runner_id')
        self.responsible_pitcher_id = kwargs.get('responsible_pitcher_id')
        self.base_before_play = kwargs.get('base_before_play')
        self.base_after_play = kwargs.get('base_after_play')
        self.was_base_stolen = kwargs.get('was_base_stolen')
        self.was_caught_stealing = kwargs.get('was_caught_stealing')
        self.was_picked_off = kwargs.get('was_picked_off')
