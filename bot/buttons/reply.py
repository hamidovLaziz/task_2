from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_button():
    design = [
        [
            KeyboardButton(text='Filial'),
            KeyboardButton(text='Start')
        ],
        [
            KeyboardButton(text='Admin')
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)


def begin_button():
    design = [
        [
            KeyboardButton(text=' Woman'),
            KeyboardButton(text=' Man')
        ],
        [
            KeyboardButton(text=' Back')
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)

def man_button():
    design = [
        [
            KeyboardButton(text=' Woman'),
            KeyboardButton(text=' Man')
        ],
        [
            KeyboardButton(text=' Back')
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)

def women_button():
    design = [
        [
            KeyboardButton(text=' Woman'),
            KeyboardButton(text=' Man')
        ],
        [
            KeyboardButton(text=' Back')
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True)
