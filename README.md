# DiceMaster 🤖🎲

**DiceMaster** is a Telegram bot designed to make your **Dungeons & Dragons (D&D)** games easier and more fun by automating dice rolls. No more searching for physical dice — just type your commands and let DiceMaster do the rolling for you!

---

## Features

* Roll standard D&D dice: `d4`, `d6`, `d8`, `d10`, `d12`, `d20`
* Roll multiple dice at once, e.g., `3d6`
* Support for modifiers, e.g., `2d8 + 3`
* Automatic critical hits and fumbles detection (for `d20`)
* Quick access to common rolls and custom macros
* Lightweight and fast — perfect for Telegram chats

---

## How to Use

1. Add DiceMaster to your Telegram: [@DiceMasterBot](https://t.me/DiceMasterBot)
2. Start the bot with `/start`
3. Roll dice using simple commands:

```
/roll d20
/roll 3d6
/roll 2d8 + 3
```

4. DiceMaster will return the results instantly in the chat.

---

## Commands

| Command  | Description                                   |
| -------- | --------------------------------------------- |
| `/start` | Start the bot and see basic instructions      |
| `/roll`  | Roll dice, e.g., `/roll d20` or `/roll 2d6+1` |
| `/help`  | Display help and command usage                |
| `/about` | Information about DiceMaster                  |

---

## Installation & Setup (for developers)

1. Clone the repository:

```bash
git clone https://github.com/yourusername/DiceMaster.git
cd DiceMaster
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your **Telegram bot token** as an environment variable:

```bash
export TELEGRAM_TOKEN="YOUR_BOT_TOKEN_HERE"  # Linux / Mac
set TELEGRAM_TOKEN=YOUR_BOT_TOKEN_HERE       # Windows
```

4. Run the bot:

```bash
python bot.py
```

---

## Contributing

Contributions are welcome!

* Fork the repository
* Create a new branch for your feature
* Submit a pull request


