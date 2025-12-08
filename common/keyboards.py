from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Кидаю кубик")]
],                  
                            resize_keyboard=True,
                            input_field_placeholder="Проверь свою удачу!")


dice_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="D4", callback_data="dice:4"),
     InlineKeyboardButton(text="D6", callback_data="dice:6")],
    [InlineKeyboardButton(text="D8", callback_data="dice:8"),
     InlineKeyboardButton(text="D10", callback_data="dice:10")],
    [InlineKeyboardButton(text="D12", callback_data="dice:12"),
     InlineKeyboardButton(text="D100", callback_data="dice:100")],
    [InlineKeyboardButton(text="D20", callback_data="dice:20")]
],
                            resize_keyboard=True,
                            input_field_placeholder="Киньте кубик")


roll_count_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="1 раз", callback_data="rolls:1")],
    [InlineKeyboardButton(text="2 раза", callback_data="rolls:2")],
    [InlineKeyboardButton(text="3 раза", callback_data="rolls:3")],
    [InlineKeyboardButton(text="4 раза", callback_data="rolls:4")],
    [InlineKeyboardButton(text="5 раз", callback_data="rolls:5")]
])