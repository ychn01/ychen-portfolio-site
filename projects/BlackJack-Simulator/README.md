# Blackjack Simulator

## Overview
Runs a simulation of a Blackjack game using soft and hard strategies over 20,000 iterations.  
Outputs win, loss, and push rates for both the player and the house.

## Project Structure

### `deck.py`
Creates a `Deck` class with:
- `deal()` — returns cards from the deck
- `get_card_value()` — calculates the value of a card

### `player.py`
Defines a `Player` class with:
- `hit()` — determines the next action based on strategy

### `simulation.py`
Main file that:
- Controls the Blackjack game logic
- Runs simulations with predefined strategies
