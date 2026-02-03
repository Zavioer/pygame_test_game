# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the Game

```bash
source .venv/bin/activate
python game.py
```

Uses `uv` as the Python manager. Install packages with `uv pip install`, e.g.:

```bash
uv pip install pygame
```

Requires Python 3.8+ and pygame.

No build, test, or lint tooling is configured.

## Architecture

This is a simple pygame game called "Catch a Bottle!" where a player catches falling bottles to score points.

**Two source files:**

- `game.py` — Entry point. Contains the `Game` class which manages the full game lifecycle: window setup (640x480, 60 FPS), start screen, main gameplay loop, collision detection (AABB), difficulty scaling (speed increases every 5 catches), game over screen, and audio playback.
- `player.py` — Defines three classes: `GameObject` (base), `Player` (keyboard-controlled character with HP/points, moves with A/D keys, SPACE for sprint), and `Enemy` (falling bottle with configurable speed).

**Game flow:** `Game.__init__()` → `start_screen()` → `main()` (gameplay loop) → `game_over_screen()` → loops back to start.

**Assets:** `pictures/` (PNG sprites and UI buttons with active/inactive states), `sounds/` (WAV effects for catch and game over).

## Known Issues

- File paths use Windows-style backslashes (e.g., `pictures\background.png`) — may break on Linux/macOS
- `player.py` has a debug `print(self.hp)` call in `Player.draw()` that fires every frame
- Typo in method name: `default_valuse()` should be `default_values()`
