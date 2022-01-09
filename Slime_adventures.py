import arcade
import time
import random
import csv

BLOCK_PIXELS = 45  #the size of tile sprites is fixed (45x45)

#game preferences
screen_width = 640
screen_height = 640
n_horizontal_blocks = 8
n_vertical_blocks = 8

#calculations
block_size_1 = screen_width/n_horizontal_blocks
block_size_2 = screen_height/n_vertical_blocks
if(block_size_1 < block_size_2):
	block_size = block_size_1
else:
	block_size = block_size_2
scaling = block_size/BLOCK_PIXELS


class MenuView(arcade.View):
	def on_show(self):
		arcade.set_background_color(arcade.color.BLACK)
		self.texture = arcade.load_texture("Menu/menu.jpg")

	def on_draw(self):
		arcade.start_render()
		self.texture.draw_sized(screen_width/2, screen_height/2, screen_width, screen_height)
		arcade.draw_text("Menu Screen", screen_width/2, screen_height/2, arcade.color.WHITE, font_size = 50, anchor_x = "center")
		arcade.draw_text("START", screen_width/2, screen_height/2 - 75, arcade.color.WHITE, font_size = 20, anchor_x = "center")
		arcade.draw_text("STAGE SELECT", screen_width/2, screen_height/2 - 150, arcade.color.WHITE, font_size = 20, anchor_x = "center")
		arcade.draw_text("INSTRUCTIONS", screen_width/2, screen_height/2 - 225, arcade.color.WHITE, font_size = 20, anchor_x = "center")
		arcade.draw_text("QUIT", screen_width/2, screen_height/2 - 300, arcade.color.WHITE, font_size = 20, anchor_x = "center")

	def on_mouse_press(self, _x, _y, _button, _modifiers):
		if((_x <= screen_width/2 + 50) and (_x >= screen_width/2 - 50) and (_y <= screen_height/2 - 75 + 20) and (_y >= screen_height/2 - 75 - 20)):  #start
			game = MyGame()
			game.setup()
			self.window.show_view(game)
		if((_x <= screen_width/2 + 50) and (_x >= screen_width/2 - 50) and (_y <= screen_height/2 - 150 + 20) and (_y >= screen_height/2 - 150 - 20)):  #stage select
			stage = StageSelect()
			self.window.show_view(stage)
		if((_x <= screen_width/2 + 50) and (_x >= screen_width/2 - 50) and (_y <= screen_height/2 - 225 + 20) and (_y >= screen_height/2 - 225 - 20)): #instructions
			inst = Instructions()
			self.window.show_view(inst)
		if((_x <= screen_width/2 + 50) and (_x >= screen_width/2 - 50) and (_y <= screen_height/2 - 300 + 20) and (_y >= screen_height/2 - 300 - 20)):  #quit
			ex = True
			game = MyGame(ex)
			game.setup()
			self.window.show_view(game)


class StageSelect(arcade.View):
	def on_show(self):
		arcade.set_background_color(arcade.color.BLACK)
		self.texture = arcade.load_texture("Menu/menu.jpg")
		self.stage11 = arcade.load_texture("Menu/Level_11.png")
		self.stage12 = arcade.load_texture("Menu/Level_12.png")
		self.stage13 = arcade.load_texture("Menu/Level_13.png")
		self.stage21 = arcade.load_texture("Menu/Level_21.png")
		self.stage22 = arcade.load_texture("Menu/Level_22.png")
		self.stage23 = arcade.load_texture("Menu/Level_23.png")
		self.stage31 = arcade.load_texture("Menu/Level_31.png")
		self.stage32 = arcade.load_texture("Menu/Level_32.png")
		self.stage33 = arcade.load_texture("Menu/Level_33.png")
		self.unknown = arcade.load_texture("Menu/unknown.png")

	def on_draw(self):
		arcade.start_render()
		self.texture.draw_sized(screen_width/2, screen_height/2, screen_width, screen_height)
		self.stage11.draw_sized(screen_width/2 - 120, screen_height/2 + 120, 100, 100)
		self.stage12.draw_sized(screen_width/2, screen_height/2 + 120, 100, 100)
		self.stage11.draw_sized(screen_width/2 + 120, screen_height/2 + 120, 100, 100)
		self.stage21.draw_sized(screen_width/2 - 120, screen_height/2, 100, 100)
		self.stage22.draw_sized(screen_width/2, screen_height/2, 100, 100)
		self.stage23.draw_sized(screen_width/2 + 120, screen_height/2, 100, 100)
		self.stage31.draw_sized(screen_width/2 - 120, screen_height/2 - 120, 100, 100)
		self.stage32.draw_sized(screen_width/2, screen_height/2 - 120, 100, 100)
		self.stage33.draw_sized(screen_width/2 + 120, screen_height/2 - 120, 100, 100)
		self.unknown.draw_sized(screen_width/2 - 120, screen_height/2 - 240, 100, 100)
		self.unknown.draw_sized(screen_width/2, screen_height/2 - 240, 100, 100)
		self.unknown.draw_sized(screen_width/2 + 120, screen_height/2 - 240, 100, 100)

		arcade.draw_text("Stage Select", screen_width/2, screen_height/2 + 240, arcade.color.WHITE, font_size = 50, anchor_x = "center")
		arcade.draw_text("FOREST", screen_width/2 - 240, screen_height/2 + 120, arcade.color.AO, font_size = 15, anchor_x = "center")
		arcade.draw_text("MOUNTAIN", screen_width/2 - 240, screen_height/2, arcade.color.BROWN, font_size = 15, anchor_x = "center")
		arcade.draw_text("ARCTIC", screen_width/2 - 240, screen_height/2 - 120, arcade.color.BLIZZARD_BLUE, font_size = 15, anchor_x = "center")
		arcade.draw_text("Find all 3 globes to unlock the hidden stage", screen_width/2, screen_height/2 - 300, arcade.color.RED, font_size = 10, anchor_x = "center")
		arcade.draw_text("Back", screen_width/2+250, screen_height/2-300, arcade.color.RED, font_size = 16, anchor_x = "center")

	def on_mouse_press(self, _x, _y, _button, _modifiers):
		level = 0
		if((_x <= screen_width/2 - 120 + 60) and (_x > screen_width/2 - 120 - 60) and (_y <= screen_height/2 + 120 + 60) and (_y > screen_height/2 + 120 - 60)):
			level = 1
		if((_x <= screen_width/2 + 60) and (_x > screen_width/2 - 60) and (_y <= screen_height/2 + 120 + 60) and (_y > screen_height/2 + 120 - 60)):
			level = 2
		if((_x <= screen_width/2 + 120 + 60) and (_x > screen_width/2 + 120 - 60) and (_y <= screen_height/2 + 120 + 60) and (_y > screen_height/2 + 120 - 60)):
			level = 3
		if((_x <= screen_width/2 - 120 + 60) and (_x > screen_width/2 - 120 - 60) and (_y <= screen_height/2 + 60) and (_y > screen_height/2 - 60)):
			level = 4
		if((_x <= screen_width/2 + 60) and (_x > screen_width/2 - 60) and (_y <= screen_height/2 + 60) and (_y > screen_height/2 - 60)):
			level = 5
		if((_x <= screen_width/2 + 120 + 60) and (_x > screen_width/2 + 120 - 60) and (_y <= screen_height/2 + 60) and (_y > screen_height/2 - 60)):
			level = 6
		if((_x <= screen_width/2 - 120 + 60) and (_x > screen_width/2 - 120 - 60) and (_y <= screen_height/2 - 120 + 60) and (_y > screen_height/2 - 120 - 60)):
			level = 7
		if((_x <= screen_width/2 + 60) and (_x > screen_width/2 - 60) and (_y <= screen_height/2 - 120 + 60) and (_y > screen_height/2 - 120 - 60)):
			level = 8
		if((_x <= screen_width/2 + 120 + 60) and (_x > screen_width/2 + 120 - 60) and (_y <= screen_height/2 - 120 + 60) and (_y > screen_height/2 - 120 - 60)):
			level = 9
		if((_x <= screen_width/2 + 250 + 20) and (_x > screen_width/2 + 250 - 20) and (_y <= screen_height/2 - 300 + 20) and (_y > screen_height/2 - 300 - 20)):  #back button
			menu = MenuView()
			self.window.show_view(menu)
		if(level > 0):
			game = MyGame(level = level - 1)
			game.setup()
			self.window.show_view(game)


class Instructions(arcade.View):
	def on_show(self):
		arcade.set_background_color(arcade.color.BLACK)
		self.texture = arcade.load_texture("Menu/instructions.png")

	def on_draw(self):
		arcade.start_render()
		self.texture.draw_sized(screen_width/2, screen_height/2, screen_width, screen_height)

	def on_mouse_press(self, _x, _y, _button, _modifiers):
		menu = MenuView()
		self.window.show_view(menu)


class Gameover(arcade.View):
		def on_show(self):
			self.texture = arcade.load_texture("Menu/gameover.png")

		def on_draw(self):
			arcade.start_render()
			self.texture.draw_sized(screen_width/2, screen_height/2, screen_width, screen_height)
			arcade.draw_text("Game Over", screen_width/2, screen_height/2, arcade.color.RED, font_size = 50, anchor_x = "center")
		
		def on_mouse_press(self, _x, _y, _button, _modifiers):
			menu = MenuView()
			self.window.show_view(menu)


#level data lists
lvlcords = []
coordinates11 = []
coordinates12 = []
coordinates13 = []

coordinates21 = []
coordinates22 = []
coordinates23 = []

coordinates31 = []
coordinates32 = []
coordinates33 = []

coordinates41 = []
coordinates42 = []
coordinates43 = []

lever_relations = [[[0, 1, 2], [1, 0, 3], [2, 0, 3], [3, 1, 2]], [[0, 3, 4], [1, 2, 4], [2, 1, 3], [3, 0, 2], [4, 0, 1]], [[0, 1, 6], [1, 6, 7], [2, 3, 4], [3, 2, 5], [4, 2, 5], [5, 3, 4], [6, 0, 7], [7, 1, 6]]]  #levels 10-11-12

#loading data
with open("Level_data/Level_11.csv", "r") as lvl:
	csvreader = csv.reader(lvl)
	for row in csvreader:
		coordinates11.append(row)
with open("Level_data/Level_12.csv", "r") as lvl:
	csvreader = csv.reader(lvl)
	for row in csvreader:
		coordinates12.append(row)
with open("Level_data/Level_13.csv", "r") as lvl:
	csvreader = csv.reader(lvl)
	for row in csvreader:
		coordinates13.append(row)
with open("Level_data/Level_21.csv", "r") as lvl:
	csvreader = csv.reader(lvl)
	for row in csvreader:
		coordinates21.append(row)
with open("Level_data/Level_22.csv", "r") as lvl:
	csvreader = csv.reader(lvl)
	for row in csvreader:
		coordinates22.append(row)
with open("Level_data/Level_23.csv", "r") as lvl:
	csvreader = csv.reader(lvl)
	for row in csvreader:
		coordinates23.append(row)
with open("Level_data/Level_31.csv", "r") as lvl:
	csvreader = csv.reader(lvl)
	for row in csvreader:
		coordinates31.append(row)
with open("Level_data/Level_32.csv", "r") as lvl:
	csvreader = csv.reader(lvl)
	for row in csvreader:
		coordinates32.append(row)
with open("Level_data/Level_33.csv", "r") as lvl:
	csvreader = csv.reader(lvl)
	for row in csvreader:
		coordinates33.append(row)
with open("Level_data/Level_41.csv", "r") as lvl:
	csvreader = csv.reader(lvl)
	for row in csvreader:
		coordinates41.append(row)
with open("Level_data/Level_42.csv", "r") as lvl:
	csvreader = csv.reader(lvl)
	for row in csvreader:
		coordinates42.append(row)
with open("Level_data/Level_43.csv", "r") as lvl:
	csvreader = csv.reader(lvl)
	for row in csvreader:
		coordinates43.append(row)

#merge into a large list
lvlcords.append(coordinates11)
lvlcords.append(coordinates12)
lvlcords.append(coordinates13)
lvlcords.append(coordinates21)
lvlcords.append(coordinates22)
lvlcords.append(coordinates23)
lvlcords.append(coordinates31)
lvlcords.append(coordinates32)
lvlcords.append(coordinates33)
lvlcords.append(coordinates41)
lvlcords.append(coordinates42)
lvlcords.append(coordinates43)

#tile namelist
tilelist = ["Vectors/Tiles/forest_1_square.png", "Vectors/Tiles/mountain_1_square.png", "Vectors/Tiles/ice_packed_square.png", "Vectors/Tiles/mountain_3_square.png"]
water_tilelist = ["Vectors/Tiles/water_forest_square.png", "Vectors/Tiles/water_mountain_square.png", "Vectors/Tiles/water_ice_square.png", "Vectors/Tiles/water_forest_square.png"]


class Slime(arcade.Sprite):
	def __init__(self, starting_x = 0, starting_y = 0):

		#set up parent class
		super().__init__("Vectors/Slime/slime_green.png", center_x = starting_x, center_y = starting_y)
		self.scale = scaling*0.5
		self.current_texture_no = 0
		self.previous_colour = "green"
		self.completed_change = True
		self.last_texture_time = 0
		self.flashing = 0
		self.flashing_colour = "red"
		self.start_flashing = 0  #when it started flashing
		self.invincible = False
		self.max_health = 1
		self.cur_health = self.max_health
		self.health_timer = 2  #seconds before death
		self.attack_time = 20000000000  #random high value

	def change_texture(self, colour = "green", flashing = 0):
		self.flashing = flashing
		if(self.flashing > 0):
			self.completed_change = True
			self.flashing_colour = colour
			if(time.time() - self.start_flashing < self.flashing):
				if(time.time() - self.last_texture_time > 0.2):
					self.completed_change = False
					self.current_texture_no = (self.current_texture_no + 1)%2
					self.last_texture_time = time.time()
					if(self.current_texture_no == 0):
						self.texture = arcade.load_texture("Vectors/Slime/slime_green.png")
					else:
						self.texture = arcade.load_texture("Vectors/Slime/slime_{}.png".format(self.flashing_colour))
			else:
				self.change_texture(self.previous_colour)
		else:
			self.texture = arcade.load_texture("Vectors/Slime/slime_{}.png".format(colour))
			self.completed_change = True
			self.flashing = 0
			self.previous_colour = colour

	def attacked(self, source = "hit", enemy = None):  #returns True for gameover or False for continue game
		if(source == "touch"):
			if(self.invincible):
				enemy.kill()
				self.change_texture(colour = self.previous_colour)
				self.invincible = False
				print("You are not invincible anymore.")
				return False
			else:
				return True
		elif(source == "skull" or source == "magma"):
			return True
		else:
			self.change_texture(colour = "green")
			self.start_flashing = time.time()
			self.change_texture(colour = "red", flashing = 1.5)
			self.cur_health -= 1
			if(self.cur_health <= 0):
				return True
			else:
				return False


class Chest(arcade.Sprite):
	def __init__(self, content, starting_x = 0, starting_y = 0):
		
		#set up parent class
		super().__init__("Vectors/Chest/chest_locked.png", center_x = starting_x, center_y = starting_y)
		self.scale = scaling*0.22
		self.content = content
		self.picked = False

	def pick_content(self):
		if(not self.picked):
			self.picked = True
			self.texture = arcade.load_texture("Vectors/Chest/chest_{}.png".format(self.content))


class Portal(arcade.Sprite):
	def __init__(self, tp, lock = False, starting_x = 0, starting_y = 0):
		
		#set up parent class
		super().__init__("Vectors/Portal/finish.png", center_x = starting_x, center_y = starting_y)
		self.type = tp
		self.scale = scaling
		self.lock = lock


class Tree(arcade.Sprite):
	def __init__(self, starting_x = 0, starting_y = 0, n_texture = 2):
		
		#set up parent class
		super().__init__("Vectors/Trees/realistic_trees_{}.png".format(n_texture), center_x = starting_x, center_y = starting_y)
		self.scale = scaling*0.9


class Pool(arcade.Sprite):
	def __init__(self, tp, stg = 1, starting_x = 0, starting_y = 0):
		#set up parent class
		if(tp == "water"):
			super().__init__(water_tilelist[stg - 1], center_x = starting_x, center_y = starting_y)
		elif(tp == "ice"):
			super().__init__("Vectors/Tiles/ice_lake_square.png", center_x = starting_x, center_y = starting_y)
		else:
			super().__init__("Vectors/Tiles/magma_square.png", center_x = starting_x, center_y = starting_y)
		self.scale = scaling
		self.type = tp
		self.start_sliding = 0  #when it started sliding

	def sliding(self, speed = 3, dt = 0.016666):
		duration = 1/(1/dt*speed/block_size)  #duration needed to travel 1 block
		if(time.time() - self.start_sliding > 2*duration):  #ensure you can't slide twice on the same ice lake for a while
			return True
		else:
			return False


class Lever(arcade.Sprite):
	def __init__(self, state, _id = 0, starting_x = 0, starting_y = 0):
		
		#set up parent class
		super().__init__("Vectors/Lever/lever_{}.png".format(state), "left", center_x = starting_x, center_y = starting_y)
		self.scale = scaling
		self.state = state
		self._id = _id
		self.last_texture_time = 0

	def change_state(self):
		if(time.time() - self.last_texture_time > 1.5):
			if(self.state == "up"):
				self.state = "left"
				self.texture = arcade.load_texture("Vectors/Lever/lever_{}.png".format(self.state))
			else:
				self.state = "up"
				self.texture = arcade.load_texture("Vectors/Lever/lever_{}.png".format(self.state))
			self.last_texture_time = time.time()


class Archer(arcade.Sprite):
	def __init__(self, starting_x = 0, starting_y = 0, rotation = 0):
		
		#set up parent class
		self.flip = False
		if(rotation == 180):
			self.flip = True
		super().__init__("Vectors/Archer/archer_1.png", center_x = starting_x + 0.06*block_size, center_y = starting_y + 0.15*block_size, flipped_horizontally = self.flip)
		if(not self.flip):
			self.angle = rotation
		self.scale = scaling*1.2
		self.current_texture = 0
		self.last_texture_time = time.time()
		self.killed = False

		#textures
		self.texture_list = []
		for i in range(11):
			self.texture_list.append(arcade.load_texture("Vectors/Archer/archer_{}.png".format(i + 1), flipped_horizontally = self.flip))
	
	def change_texture(self):
		if(time.time() - self.last_texture_time > 0.1):
			if(self.current_texture == len(self.texture_list) - 1):
				self.killed = True
				self.current_texture = 0
			else:
				self.current_texture += 1
			self.last_texture_time = time.time()
			self.texture = self.texture_list[self.current_texture]

	def inrange(self, slime):  #check if slime is in range
		if(not self.flip and slime.center_x > self.center_x + block_size/2 and abs(slime.center_y - self.center_y) < block_size/2):  #right
			return True
		elif(self.flip and slime.center_x < self.center_x - block_size/2 and abs(slime.center_y - self.center_y) < block_size/2):  #left
			return True
		else:
			return False


class Knight(arcade.Sprite):
	def __init__(self, starting_x = 0, starting_y = 0, rotation = 0):
		
		#set up parent class
		self.flip = False
		if(rotation == 180):
			self.flip = True
		super().__init__("Vectors/Knight/knight_1.png", center_x = starting_x + 0.06*block_size, center_y = starting_y + 0.03*block_size, flipped_horizontally = self.flip)
		if(not self.flip):
			self.angle = rotation
		self.scale = scaling
		self.current_texture = 0
		self.last_texture_time = time.time()
		self.killed = False

		#textures
		self.texture_list = []
		for i in range(9):
			self.texture_list.append(arcade.load_texture("Vectors/Knight/knight_{}.png".format(i + 1), flipped_horizontally = self.flip))
	
	def change_texture(self):
		if(time.time() - self.last_texture_time > 0.1):
			if(self.current_texture == len(self.texture_list) - 1):
				self.current_texture = 0
				self.killed = True
			else:
				self.current_texture += 1
			self.last_texture_time = time.time()
			self.texture = self.texture_list[self.current_texture]

	def inrange(self, slime):  #check if slime is in range
		if(not self.flip and slime.center_x < self.center_x + block_size and abs(slime.center_y - self.center_y) < block_size/2 and slime.center_x > self.center_x):  #left
			return True
		elif(self.flip and slime.center_x < self.center_x and abs(slime.center_y - self.center_y) < block_size/2 and slime.center_x > self.center_x - 2*block_size):  #right
			return True
		else:
			return False


class Mage(arcade.Sprite):
	def __init__(self, starting_x = 0, starting_y = 0, rotation = 0):
		
		#set up parent class
		self.flip = False
		if(rotation == 180):
			self.flip = True
		super().__init__("Vectors/Mage/mage_1.png", center_x = starting_x, center_y = starting_y, flipped_horizontally = self.flip)
		if(not self.flip):
			self.angle = rotation
		self.scale = scaling*1.55
		self.current_texture = 0
		self.last_texture_time = time.time()
		self.killed = False

		#textures
		self.texture_list = []
		for i in range(9):
			self.texture_list.append(arcade.load_texture("Vectors/Mage/mage_{}.png".format(i + 1), flipped_horizontally = self.flip))
	
	def change_texture(self):
		if(time.time() - self.last_texture_time > 0.1):
			if(self.current_texture == len(self.texture_list) - 1):
				self.killed = True
				self.current_texture = 0
			else:
				self.current_texture += 1
			self.last_texture_time = time.time()
			self.texture = self.texture_list[self.current_texture]

	def inrange(self, slime):  #check if slime is in range
		if(not self.flip and slime.center_x > self.center_x + block_size/2 and abs(slime.center_y - self.center_y) < block_size/2):  #right
			return True
		elif(self.flip and slime.center_x < self.center_x - block_size/2 and abs(slime.center_y - self.center_y) < block_size/2):  #left
			return True
		else:
			return False


class Crusader(arcade.Sprite):
	def __init__(self, starting_x = 0, starting_y = 0):
		
		#set up parent class
		super().__init__("Vectors/Crusader/crusader_1.png", center_x = starting_x, center_y = starting_y + 0.15*block_size)
		self.scale = scaling*1.6
		self.current_texture = 0
		self.last_texture_time = time.time()
		self.killed = False

		#textures
		self.texture_list = []
		for i in range(14):
			self.texture_list.append(arcade.load_texture("Vectors/Crusader/crusader_{}.png".format(i + 1)))
	
	def change_texture(self):
		if(time.time() - self.last_texture_time > 0.1):
			if(self.current_texture == len(self.texture_list) - 1):
				self.current_texture = 0
				self.killed = True
			else:
				self.current_texture += 1
			self.last_texture_time = time.time()
			self.texture = self.texture_list[self.current_texture]

	def inrange(self, slime):  #check if slime is in range
		if((abs(slime.center_x - self.center_x) < 1.5*block_size) and (abs(slime.center_y - self.center_y) < 0.5*block_size)):  #1 block left or right - same y
			return True
		if((abs(slime.center_y - self.center_y) < 1.5*block_size) and (abs(slime.center_x - self.center_x) < 0.5*block_size)):  #1 block up or down - same x
			return True
		else:
			return False


class MyGame(arcade.View):
	def __init__(self, ex = False, level = 0, globes = 0):
		#initialise game window and basic parameters to use
		super().__init__()
		self.exit = ex
		self.level = level
		
		#sprite lists
		self.slime_list = None
		self.tile_list = None
		self.prop_list = None
		self.enemy_list = None
		self.next_x = 0
		self.next_y = 0
		self.globes = globes  #how many found
		self.gameover = False

	def setup(self):
		#sprite lists
		self.slime_list = arcade.SpriteList()
		self.tile_list = arcade.SpriteList()
		self.prop_list = arcade.SpriteList()
		self.enemy_list = arcade.SpriteList()
		stage = self.level//3 + 1  #1 stage contains 3 levels

		#generating tiles
		for x in range(0, n_horizontal_blocks):
			for y in range(0, n_vertical_blocks):
				tile = arcade.Sprite(tilelist[stage - 1], center_x = x*block_size + block_size/2, center_y = y*block_size + block_size/2, scale = scaling)
				self.tile_list.append(tile)

		self.lever_count = 0
		#generating objects
		for i in range(len(lvlcords[self.level][0])):
			for j in range(len(lvlcords[self.level])):
				if(lvlcords[self.level][i][j] == 'P'):  #pool
					self.prop_list.append(Pool(tp = "water", starting_x = i*block_size + block_size/2, starting_y = j*block_size + block_size/2, stg = stage))
				elif(lvlcords[self.level][i][j] == 'IL'):  #ice lake
					self.prop_list.append(Pool(tp = "ice", starting_x = i*block_size + block_size/2, starting_y = j*block_size + block_size/2))
				elif(lvlcords[self.level][i][j] == 'M'):  #magma
					self.prop_list.append(Pool(tp = "magma", starting_x = i*block_size + block_size/2, starting_y = j*block_size + block_size/2))
				elif(lvlcords[self.level][i][j] == 'S'):  #start
					self.slime_list.append(Slime(starting_x = i*block_size + block_size/2, starting_y = j*block_size + block_size/2))
				elif(lvlcords[self.level][i][j] == 'A+'):  #archer right
					self.enemy_list.append(Archer(starting_x = i*block_size + block_size/2, starting_y = j*block_size + block_size/2))
				elif(lvlcords[self.level][i][j] == 'A-'):  #archer left
					self.enemy_list.append(Archer(starting_x = i*block_size + block_size/2, starting_y = j*block_size + block_size/2, rotation = 180))
				if(lvlcords[self.level][i][j] == 'K+'):  #knight right
					self.enemy_list.append(Knight(starting_x = i*block_size + block_size/2, starting_y = j*block_size + block_size/2))
				elif(lvlcords[self.level][i][j] == 'K-'):  #knight left
					self.enemy_list.append(Knight(starting_x = i*block_size + block_size/2, starting_y = j*block_size + block_size/2, rotation = 180))
				elif(lvlcords[self.level][i][j] == 'C'):  #crusader
					self.enemy_list.append(Crusader(starting_x = i*block_size + block_size/2, starting_y = j*block_size + block_size/2))
				elif(lvlcords[self.level][i][j] == 'T'):  #tree
					self.prop_list.append(Tree(starting_x = i*block_size + block_size/2, starting_y = j*block_size + block_size/2, n_texture = random.randint(1, 4)))
				elif(lvlcords[self.level][i][j] == 'M+'):  #mage right
					self.enemy_list.append(Mage(starting_x = i*block_size + block_size/2, starting_y = j*block_size + block_size/2))
				elif(lvlcords[self.level][i][j] == 'M-'):  #mage left
					self.enemy_list.append(Mage(starting_x = i*block_size + block_size/2, starting_y = j*block_size + block_size/2, rotation = 180))
				elif(lvlcords[self.level][i][j] == 'F'):  #finish portal
					self.prop_list.append(Portal(tp = "finish", starting_x = i*block_size + block_size/2, starting_y = j*block_size + block_size/2))
				elif(lvlcords[self.level][i][j] == 'FL'):  #locked finish portal
					self.prop_list.append(Portal(tp = "finish", lock = True, starting_x = i*block_size + block_size/2, starting_y = j*block_size + block_size/2))
				elif(lvlcords[self.level][i][j] == 'LL'):  #lever left
					self.prop_list.append(Lever(state = "left", _id = self.lever_count, starting_x = i*block_size + block_size/2, starting_y = j*block_size + block_size/2))
					self.lever_count += 1
				elif(lvlcords[self.level][i][j] == 'LU'):  #lever up
					self.prop_list.append(Lever(state = "up", _id = self.lever_count, starting_x = i*block_size + block_size/2, starting_y = j*block_size + block_size/2))
					self.lever_count += 1
				elif(lvlcords[self.level][i][j] == 'CHE'):  #empty chest
					self.prop_list.append(Chest(content = "empty", starting_x = i*block_size + block_size/2, starting_y = j*block_size + block_size/2))
				elif(lvlcords[self.level][i][j] == 'CHC'):  #chest with a crown
					self.prop_list.append(Chest(content = "crown", starting_x = i*block_size + block_size/2, starting_y = j*block_size + block_size/2))
				elif(lvlcords[self.level][i][j] == 'CHG'):  #chest with a globe
					self.prop_list.append(Chest(content = "globe", starting_x = i*block_size + block_size/2, starting_y = j*block_size + block_size/2))
				elif(lvlcords[self.level][i][j] == 'CHS'):  #chest with a skull
					self.prop_list.append(Chest(content = "skull", starting_x = i*block_size + block_size/2, starting_y = j*block_size + block_size/2))

	def on_draw(self):
		arcade.start_render()  #always first

		#draw all the sprites
		self.tile_list.draw()
		self.prop_list.draw()
		self.slime_list.draw()
		#self.prop_list.draw()
		self.enemy_list.draw()

	def on_key_press(self, key, modifiers):
		if(self.slime_list[0].change_y == 0 and self.slime_list[0].change_x == 0):
			if(key == arcade.key.UP or key == arcade.key.W):
				self.next_y = self.slime_list[0].center_y + block_size
				if(self.next_y > n_vertical_blocks*block_size):  #check boundaries
					self.next_y = self.slime_list[0].center_y
				self.slime_list[0].change_y = 3
			if(key == arcade.key.DOWN or key == arcade.key.S):
				self.next_y = self.slime_list[0].center_y - block_size
				if(self.next_y < 0):  #check boundaries
					self.next_y = self.slime_list[0].center_y
				self.slime_list[0].change_y = -3
			if(key == arcade.key.LEFT or key == arcade.key.A):
				self.next_x = self.slime_list[0].center_x - block_size
				if(self.next_x < 0):  #check boundaries
					self.next_x = self.slime_list[0].center_x
				self.slime_list[0].change_x = -3
			if(key == arcade.key.RIGHT or key == arcade.key.D):
				self.next_x = self.slime_list[0].center_x + block_size
				if(self.next_x > n_horizontal_blocks*block_size):  #check boundaries
					self.next_x = self.slime_list[0].center_x
				self.slime_list[0].change_x = 3

	def update(self, delta_time):
		if(self.exit):  #menu quit
			exit()
		if(self.gameover):  #gameover
			self.over()

		#slime updates
		self.slime_list.update()
		if((not self.slime_list[0].completed_change) or (self.slime_list[0].flashing > 0)):  #complete texture change
			self.slime_list[0].change_texture(colour = self.slime_list[0].flashing_colour, flashing = self.slime_list[0].flashing)
		if(time.time() - self.slime_list[0].attack_time > self.slime_list[0].health_timer):  #health timer
			self.gameover = self.slime_list[0].attacked()
			self.slime_list[0].attack_time = 20000000000

		#power-ups
		player_collision_list = arcade.check_for_collision_with_list(self.slime_list[0], self.prop_list)
		for collision in player_collision_list:
			if(type(collision) is Pool):
				if(collision.type == "water"):
					if(self.slime_list[0].attack_time != 20000000000):
						self.slime_list[0].attack_time = 20000000000
						self.slime_list[0].start_flashing = time.time()
						self.slime_list[0].change_texture(colour = "blue", flashing = 1.5)
						print("You have received water blessing and the mage's curse is lifted.")
				elif(collision.type == "ice"):  #slide on ice
					speed = max([abs(self.slime_list[0].change_x), abs(self.slime_list[0].change_y)])
					if(collision.sliding(speed, delta_time)):  #if sliding is approved for the duration needed
						collision.start_sliding = time.time()
						if(self.slime_list[0].change_x > 0):
							self.next_x += block_size						
						elif(self.slime_list[0].change_x < 0):
							self.next_x -= block_size
						elif(self.slime_list[0].change_y > 0):
							self.next_y += block_size
						elif(self.slime_list[0].change_y < 0):
							self.next_y -= block_size
				else:
					self.gameover = self.slime_list[0].attacked(source = "magma")
			elif(type(collision) is Tree):
				if(self.slime_list[0].cur_health == 1):
					print("You have obtained tree armor and you are hidden against the Archer's attack.")
					self.slime_list[0].cur_health += 1
					self.slime_list[0].change_texture(colour = "blue")
			elif(type(collision) is Lever):
				print(collision._id)
				for i in range(len(lever_relations[self.level - 10])):
					if(lever_relations[self.level - 10][i][0] == collision._id):
						same_state_count = 0
						current_state = ""
						for lever in self.prop_list:
							if(type(lever) is Lever):
								if(lever._id in lever_relations[self.level - 10][i]):
									lever.change_state()
								if(current_state == ""):
									current_state = lever.state
									same_state_count += 1
								elif(current_state == lever.state):
									same_state_count += 1
						if(self.lever_count == same_state_count):
							for portal in self.prop_list:
								if(type(portal) is Portal):
									if(portal.type == "finish"):
										portal.lock = False
										print("Portal unlocked.")
			elif(type(collision) is Chest):
				if(not collision.picked):
					collision.pick_content()
					if(collision.content == "globe"):
						self.globes += 1
						print("Total globes:", self.globes)
					elif(collision.content == "crown"):
						self.slime_list[0].invincible = True
						self.slime_list[0].change_texture(colour = "blue", flashing = 20000000000)  #flashing until enemy touched
						print("Touch an enemy to kill.")
					elif(collision.content == "skull"):
						self.gameover = self.slime_list[0].attacked(source = "skull")
						print("Unfortunately, you found a skull.")
					else:
						print("Just an empty chest.")
			elif(type(collision) is Portal):
				if(collision.type == "finish"):
					if(collision.lock == False):
						print("Congratulations! You have passed the level.")
						self.level += 1
						if(self.level <= 8):
							game = MyGame(level = self.level, globes = self.globes)
							game.setup()
							self.window.show_view(game)
						elif(self.level <= 11):
							if(self.globes >= 3):
								game = MyGame(level = self.level, globes = self.globes)
								game.setup()
								self.window.show_view(game)
							else:
								print("You need 3 globes to start this level.")
								menu = MenuView()
								self.window.show_view(menu)
						else:
							menu = MenuView()
							self.window.show_view(menu)
					else:
						print("Portal is locked.")

		#fire if in range
		for i in range(len(self.enemy_list)):
			if(self.enemy_list[i].inrange(self.slime_list[0]) or self.enemy_list[i].current_texture > 0):
				self.enemy_list[i].change_texture()
			
			#damage from attack
			if(self.enemy_list[i].killed):
				if(type(self.enemy_list[i]) is Mage):
					self.slime_list[0].attack_time = time.time()
					self.enemy_list[i].killed = False
					self.slime_list[0].start_flashing = time.time()
					self.slime_list[0].change_texture(colour = "red", flashing = self.slime_list[0].health_timer)
				else:
					self.gameover = self.slime_list[0].attacked()
					self.enemy_list[i].killed = False

		#stop slime movement
		if((self.slime_list[0].change_x > 0 and self.slime_list[0].center_x >= self.next_x) or (self.slime_list[0].change_x < 0 and self.slime_list[0].center_x <= self.next_x)):
			self.slime_list[0].change_x = 0
			self.slime_list[0].center_x = self.next_x
		if((self.slime_list[0].change_y > 0 and self.slime_list[0].center_y >= self.next_y) or (self.slime_list[0].change_y < 0 and self.slime_list[0].center_y <= self.next_y)):
			self.slime_list[0].change_y = 0
			self.slime_list[0].center_y = self.next_y

		#damage if enemy touched
		player_collision_list = arcade.check_for_collision_with_list(self.slime_list[0], self.enemy_list)
		for collision in player_collision_list:
			self.gameover = self.slime_list[0].attacked(source = "touch", enemy = collision)

	def over(self):
		print("Game Over")
		death = Gameover()
		self.window.show_view(death)


#initialise game
window = arcade.Window(screen_width, screen_height, "Slime Adventures")
menu = MenuView()
window.show_view(menu)
arcade.run()