import pygame
import time
import gamefiles.ui as ui


# Class definition
class Move:
    def __init__(self, direction):
        self.direction = direction


class Talk:
    def __init__(self, name, message):
        self.name = name
        self.message = message


# Move class
house1 = Move("Outside")

chair = Move("Beginning")
# Talk class
George = Talk("George", "Hello, i'm george. ")

Brian = Talk("Brian", "Hello , i'm brian.")


class Location:
    """This Class is used for handling the position where you are and what you can do
    and where you can
    Context_list is used to store every possible direction displayed
    location index is just to move between this list
    """
    def __init__(self, name, context_list):
        self.name = name
        self.context_list = context_list
        self.location_index = 1
        self.max_index = len(context_list)

    def return_context_name(self):
        current_selection = self.context_list[self.location_index]
        if isinstance(current_selection, Move):
            return current_selection.direction
        if isinstance(current_selection, Talk):
            return current_selection.name
        else:
            return "None"

    def return_context(self):
        current_selection = self.context_list[self.location_index]
        return current_selection


Beginning = Location("Village", [house1, George])
Outside = Location("Outside", [chair, Brian])

actual = Beginning
every = {"Village": Beginning, "Outside": Outside}

place = actual.name


def control_check(actual):
    actual.location_index = ui.button_index(actual.location_index)
    a = ui.button_action(actual.return_context(), actual)
    ui.place = a
    actual = every[a]




