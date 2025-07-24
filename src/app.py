#!/usr/bin/env python3

import app

import arcade
from GameView import GameView


def main():
    """Main function"""
    # Create a window class. This is what actually shows up on screen
    window = arcade.Window(1280, 720, "Minimal Sprite Example")

    # Create and setup the GameView
    game = GameView()

    # Show GameView on screen
    window.show_view(game)

    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    app.main()

# EOF
