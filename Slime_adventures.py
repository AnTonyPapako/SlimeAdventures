import arcade

#game preferences
screen_width = 1080
screen_height = 768

class MyGame(arcade.Window):
	def __init__(self, width, height, title):
		#initialise game window and basic parameters to use
		super().__init__(width, height, title)

	def setup(self):
		pass

	def on_draw(self):
		pass

	def on_key_press(self, key, modifiers):
		pass

	def on_key_release(self, key, modifiers):
		pass

	def update(self, delta_time):
		pass

#initialise game
game = MyGame(screen_width, screen_height, "Slime Adventures")
game.setup()
arcade.run()