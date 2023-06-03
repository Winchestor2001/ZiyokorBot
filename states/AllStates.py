from aiogram.dispatcher.filters.state import StatesGroup, State


class UserStates(StatesGroup):
    full_name = State()
    tests = State()
    start_test = State()

