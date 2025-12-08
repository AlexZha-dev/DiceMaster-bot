from aiogram.fsm.state import StatesGroup, State

class DiceState(StatesGroup):
    choose_dice = State()
    choose_rolls = State()
