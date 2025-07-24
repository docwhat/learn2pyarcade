"""
Minimal Sprite Example

Draws a single sprite in the middle screen.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_minimal
"""

import arcade

__all__ = ["GameView"]


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        # 1. Create the SpriteList
        self.sprites = arcade.SpriteList()

        # 2. Create & append your Sprite instance to the SpriteList
        self.player = arcade.Sprite(
            ":resources:images/animated_characters/female_person/femalePerson_idle.png"
        )
        self.player.position = self.center  # center sprite on screen
        self.sprites.append(self.player)  # Append the instance to the SpriteList

    def on_draw(self):
        # 3. Clear the screen
        self.clear()

        # 4. Call draw() on the SpriteList inside an on_draw() method
        self.sprites.draw()
