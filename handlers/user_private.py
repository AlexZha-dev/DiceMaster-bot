from random import randint

from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

import common.keyboards as kb
from states.dice_states import DiceState

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.reply(text="Это бот для игры в D&D", reply_markup=kb.main)


@user_private_router.message(F.text == "Кидаю кубик")
async def start_cmd(message: types.Message):
    await message.reply(text="Да благославит тебя удача", reply_markup=kb.dice_keyboard)


@user_private_router.callback_query(F.data.startswith("dice:"))
async def choose_dice(callback: types.CallbackQuery, state: FSMContext):
    sides = int(callback.data.split(":")[1])

    await state.update_data(dice_sides=sides)

    await callback.message.edit_text(
        f"Вы выбрали D{sides}. Теперь выберите количество бросков:",
        reply_markup=kb.roll_count_keyboard,
    )

    await state.set_state(DiceState.choose_rolls)


@user_private_router.callback_query(F.data.startswith("rolls:"))
async def make_roll(callback: types.CallbackQuery, state: FSMContext):
    rolls = int(callback.data.split(":")[1])

    data = await state.get_data()
    sides = data.get("dice_sides")

    results = [randint(1, sides) for _ in range(rolls)]
    total = sum(results)

    funny_comments = []

    for r in results:
        if sides == 20:
            if r == 1 and rolls == 1:
                funny_comments.append("1 💀 Фиаско!")
            elif r == 20 and rolls == 1:
                funny_comments.append("20 🏆 Критический успех!")
            else:
                funny_comments.append(f"{r}")
        else:
            funny_comments.append(str(r))

    results_funny = ", ".join(funny_comments)

    await callback.message.edit_text(
        f"🎲 Броски D{sides} x{rolls}\n"
        f"Результаты: {results_funny}\n"
        f"Сумма: {total}"
    )

    await state.clear()
