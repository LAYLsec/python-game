# Cosmic Dungeon Quest

A roguelike dungeon crawler game written in Python. Explore procedurally generated dungeons, fight enemies, collect loot, and get stronger.

## What's This?

It's a text-based RPG game where you go into dungeons, fight monsters, and try to survive as deep as you can. Each time you play, the dungeons are different because they're randomly generated.

## Features

- **Procedural Dungeons** - Different layout every time you play
- **Combat System** - Fight enemies with different abilities and strategies
- **Loot & Equipment** - Find better gear to get stronger
- **Leveling System** - Gain experience and level up
- **Enemy AI** - Enemies make tactical decisions, not just spam attacks
- **Multiple Biomes** - Different environments with different enemy types
- **Status Effects** - Apply bleed, burn, stun effects in combat
- **Save System** - Save your progress between sessions

## Quick Start

### Requirements
- Python 3.8 or higher (that's it, no external dependencies)

### Installation

```bash
git clone https://github.com/LAYLsec/python-game.git
cd python-game
python cosmic_dungeon_quest.py
```

That's all you need to do.

## How to Play

1. Run the game
2. Enter your character name
3. Choose from the menu (Enter Dungeon, View Stats, etc.)
4. Pick a difficulty level
5. Start fighting enemies in rooms
6. Use your abilities strategically
7. Collect loot and level up
8. Try to go deeper and deeper

### In Combat

You have 4 abilities:
- **Slash** - Basic attack
- **Power Strike** - Stronger attack with bleed effect
- **Mana Shield** - Defensive ability
- **Execute** - Powerful attack with long cooldown

Pick the right ability, manage your health, and defeat enemies.

## Game Systems

### Stats
Each character has stats that affect gameplay:
- **Health** - How much damage you can take
- **Mana** - Resource for abilities
- **Strength** - Physical damage
- **Intelligence** - Magical power
- **Dexterity** - Speed and critical hits
- **Endurance** - Defense/armor

Stats grow as you level up. Equipment also gives bonuses.

### Enemies
Different enemy types appear in different biomes:
- Goblins, Orcs, Skeletons, Demons, Drakes, Liches, Wraiths

Each has different stats and behaviors. Some will flee if losing, some will defend.

### Loot
When you kill enemies, they might drop items:
- Common (⚪) through Mythic (🔴) rarity
- Different equipment types (swords, armor, rings, etc.)
- Items have random stats based on rarity

### Biomes
6 different environments to explore:
- **Crypt** - Undead-filled dungeons
- **Inferno** - Hot lava chambers with demons
- **Frost** - Frozen wastelands
- **Abyss** - Mixed chaos
- **Forest** - Nature and beasts
- **Shadow** - Dark areas

## Tips

- Don't rush - think about your ability choices
- Balance offense and defense
- Harder difficulties give better loot
- Enemies get stronger as you go deeper
- Status effects are powerful in combat
- Different equipment combinations work for different playstyles

## Difficulty Levels

| Difficulty | Enemy Range | Max Tries | Better Loot? |
|-----------|------------|----------|------------|
| Easy | 1-50 | 15 | Yes |
| Medium | 1-100 | 10 | Normal |
| Hard | 1-200 | 7 | Yes |

## Project Files

- `cosmic_dungeon_quest.py` - The main game
- `guess_the_number.py` - Bonus simple game
- `README.md` - This file
- `CHANGELOG.md` - What changed in each version
- `LICENSE` - MIT License (you can use this freely)

## Issues or Ideas?

Found a bug? Have a cool idea? Open an issue on GitHub:
https://github.com/LAYLsec/python-game/issues

Want to contribute? Check out `CONTRIBUTING.md`.

## License

MIT License - basically you can do whatever you want with this code. See LICENSE file for details.

## Future Ideas

- Multiplayer co-op
- Boss fights with unique mechanics
- Quest system
- NPC interactions
- More biomes and enemies
- Leaderboards
- Maybe a graphical version someday

---

**Made by LAYLsec**

Have fun! 🎮
