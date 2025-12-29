from aiogram.fsm.state import State, StatesGroup


class FindProduct(StatesGroup):
    mahsulotlar = State()
    ha = State()
    yoq = State()

class tolovStates(StatesGroup):
    tolov1 = State()
    lokatsiya = State()






PRODUCTS = {
    "1": 4,
    "01": 4,
    "001": 4,
    "2": 5,
    "02": 5,
    "002": 5,
    "3": 6,
    "03": 6,
    "003": 6,
    "4": 7,
    "04": 7,
    "004": 7,
    "5": 8,
    "05": 8,
    "005": 8,
    "6": 9,
    "06": 9,
    "006": 9,
    "7": 10,
    "07": 10,
    "007": 10,
    "8": 11,
    "08": 11,
    "008": 11,
    "9": 12,
    "09": 12,
    "009": 12,
    "10": 13,
    "010": 13,
}
