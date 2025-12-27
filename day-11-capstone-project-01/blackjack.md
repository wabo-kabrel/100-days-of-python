# Blackjack Game

This is a simple console-based **Blackjack (21)** game written in Python.

## Objective
The goal of the game is to get a hand value **as close to 21 as possible without going over**.  
You play against the **dealer**.

## Card Values
- Cards **2–10** count as their face value  
- **Jack, Queen, King** count as **10**
- **Ace** counts as **1 or 11**, whichever is better for the hand

## How the Game Works
1. Both the player and dealer are dealt **two cards**
2. One of the dealer’s cards is hidden
3. The player can:
   - **Hit** → take another card
   - **Stand** → stop taking cards
4. If the player’s total exceeds **21**, the player loses
5. The dealer reveals their card and must hit until their total is **17 or higher**
6. The hand closest to **21** without exceeding it wins

## Winning Rules
- Exceeding 21 results in a loss (*bust*)
- If the dealer busts, the player wins
- Higher score wins
- Equal scores result in a draw (*push*)

## Run the Game
```bash
python blackjack.py
