from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardRemove

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="")]
],
    resize_keyboard=True,
    input_field_placeholder="Воспользуйтесь кнопками",)

pin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="", callback_data="")]
])


remove = ReplyKeyboardRemove()