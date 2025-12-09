from random import randint, choice

from aiogram import types, Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

import common.keyboards as kb
from states.dice_states import DiceState
from common.d20_responses import d20_roll_messages

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
        if sides == 20 and rolls == 1:
            if r == 1:
                comment = f"{r}\n{choice(d20_roll_messages[1])}"
            elif 2 <= r <= 4:
                comment = f"{r}\n{choice(d20_roll_messages[2])}"
            elif 5 <= r <= 8:
                comment = f"{r}\n{choice(d20_roll_messages[3])}"
            elif 9 <= r <= 12:
                comment = f"{r}\n{choice(d20_roll_messages[4])}"
            elif 13 <= r <= 16:
                comment = f"{r}\n{choice(d20_roll_messages[5])}"
            elif 17 <= r <= 19:
                comment = f"{r}\n{choice(d20_roll_messages[6])}"
            elif r == 20:
                comment = f"{r}\n{choice(d20_roll_messages[7])}"

            funny_comments.append(comment)
            results_funny = "".join(funny_comments)
        else:
            funny_comments.append(str(r))
            results_funny = ", ".join(funny_comments)

    if rolls == 1:
        text = f"🎲 Бросок D{sides}\nРезультат броска: {results_funny}"
    else:
        text = f"🎲 Броски D{sides} x{rolls}\nРезультаты бросков: {results_funny}"
        total = sum(results)
        text += f"\nСумма: {total}"

    await callback.message.edit_text(text)

    await state.clear()
