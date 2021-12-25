"""
Holds functions for buttons of all kinds
"""
class ButtonFunctionHolder:
    """
    Args:
    user_input (class UserInput)
    """

    def __init__(self, user_input):
        self.user_input = user_input

    def change_scene(self, kwargs=None):
        """
        starts a new game
        saves username from textinput to menu object
        Args:
        check user_input.py, function mouse_button_check()
        """
        kwargs['game_loop'].scene = kwargs['button_value']
        if kwargs['button_value'] == "level":
            kwargs['scene_obj'].player_name = kwargs['scene_obj'].text_input.value

    def exit(self, kwargs=None):
        """
        reh
        """
        kwargs['game_loop'].running = kwargs['button_value']

    def flip_one(self, kwargs=None):
        """
        flips the value of one_active in UserInput
        """
        kwargs['user_input'].one_active ^= 1
