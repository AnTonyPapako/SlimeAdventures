import arcade
import time
import random

BLOCK_PIXELS = 45  #the size of tile sprites are fixed (45x45)

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


class Slime(arcade.Sprite):
	def __init__(self, starting_x = 0, starting_y = 0):

		#set up parent class
		super().__init__("Vectors/Slime/slime_1.png", center_x = starting_x, center_y = starting_y)
		self.scale = scaling*0.5
		self.current_texture = 0
		self.last_texture_time = time.time()
		self.max_health = 1
		self.cur_health = self.max_health

		#textures
		self.texture_list = []
		for i in range(2):
			self.texture_list.append(arcade.load_texture("Vectors/Slime/slime_{}.png".format(i + 1)))

		def change_texture(self):
			if(time.time() - self.last_texture_time > 0.5):
				if(self.current_texture == len(self.texture_list) - 1):
					self.current_texture = 0
				else:
					self.current_texture += 1
				self.last_texture_time = time.time()
				self.texture = self.texture_list[self.current_texture]


class Tree(arcade.Sprite):
	def __init__(self, starting_x = 0, starting_y = 0, n_texture = 2):
		
		#set up parent class
		super().__init__("Vectors/Trees/realistic_trees_{}.png".format(n_texture), center_x = starting_x + 0.06*block_size, center_y = starting_y + 0.15*block_size)
		self.scale = scaling*1.0

	def inrange(self, slime):  #check if slime is in range
		if(slime.center_x < self.center_x + block_size/2 and abs(slime.center_y - self.center_y) < block_size/2 and slime.center_x > self.center_x):  #left
			return True
		elif(slime.center_x < self.center_x and abs(slime.center_y - self.center_y) < block_size/2 and slime.center_x > self.center_x - 2*block_size):  #right
			return True
		#elif(slime.center_y > self.center_y + block_size/2 and abs(slime.center_x - self.center_x) < block_size/2):  #up
			#return True
		elif(slime.center_y < self.center_y - block_size/2 and abs(slime.center_y - self.center_y) < block_size/2):  #down
			return True
		else:
			return False

	def attack(self):
		pass


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

	def attack(self):
		pass


class Knight(arcade.Sprite):
	def __init__(self, starting_x = 0, starting_y = 0, rotation = 0):
		
		#set up parent class
		self.flip = False
		if(rotation == 180):
			self.flip = True
		super().__init__("Vectors/Knight/Knight_1.png", center_x = starting_x + 0.06*block_size, center_y = starting_y + 0.09*block_size, flipped_horizontally = self.flip)
		if(not self.flip):
			self.angle = rotation
		self.scale = scaling
		self.current_texture = 0
		self.last_texture_time = time.time()
		self.killed = False

		#textures
		self.texture_list = []
		for i in range(9):
			self.texture_list.append(arcade.load_texture("Vectors/Knight/Knight_{}.png".format(i + 1), flipped_horizontally = self.flip))
	
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

	def attack(self):
		pass


class MyGame(arcade.Window):
	def __init__(self, width, height, title):
		#initialise game window and basic parameters to use
		super().__init__(width, height, title)

		#sprite lists
		self.slime_list = None
		self.tile_list = None
		self.prop_list = None
		self.enemy_list = None
		self.next_x = 0
		self.next_y = 0

	def setup(self):
		#sprite lists
		self.slime_list = arcade.SpriteList()
		self.tile_list = arcade.SpriteList()
		self.prop_list = arcade.SpriteList()
		self.enemy_list = arcade.SpriteList()

		#tile generation
		for x in range(0, n_horizontal_blocks):
			for y in range(0, n_vertical_blocks):
				tile = arcade.Sprite("Vectors/Tiles/forest_1_square.png", center_x = x*block_size + block_size/2, center_y = y*block_size + block_size/2, scale = scaling)
				self.tile_list.append(tile)

		#slime spawn coordinates
		if(n_horizontal_blocks%2 == 1):
			starting_x = n_horizontal_blocks*block_size/2
		else:
			starting_x = n_horizontal_blocks*block_size/2 + block_size/2
		if(n_vertical_blocks%2 == 1):
			starting_y = n_vertical_blocks*block_size/2
		else:
			starting_y = n_vertical_blocks*block_size/2 + block_size/2

		self.slime_list.append(Slime(starting_x = 0*block_size + block_size/2, starting_y = 6*block_size + block_size/2))
		self.prop_list.append(Tree(starting_x = 0*block_size + block_size/2, starting_y = 7*block_size + block_size/2, n_texture = random.randint(1, 4)))
		self.prop_list.append(Tree(starting_x = 0*block_size + block_size/2, starting_y = 4*block_size + block_size/2, n_texture = random.randint(1, 4)))
		self.prop_list.append(Tree(starting_x = 0*block_size + block_size/2, starting_y = 1*block_size + block_size/2, n_texture = random.randint(1, 4)))
		self.prop_list.append(Tree(starting_x = 0*block_size + block_size/2, starting_y = 0*block_size + block_size/2, n_texture = random.randint(1, 4)))
		self.prop_list.append(Tree(starting_x = 2*block_size + block_size/2, starting_y = 4*block_size + block_size/2, n_texture = random.randint(1, 4)))
		self.prop_list.append(Tree(starting_x = 3*block_size + block_size/2, starting_y = 7*block_size + block_size/2, n_texture = random.randint(1, 4)))
		self.prop_list.append(Tree(starting_x = 3*block_size + block_size/2, starting_y = 4*block_size + block_size/2, n_texture = random.randint(1, 4)))
		self.prop_list.append(Tree(starting_x = 4*block_size + block_size/2, starting_y = 5*block_size + block_size/2, n_texture = random.randint(1, 4)))
		self.prop_list.append(Tree(starting_x = 5*block_size + block_size/2, starting_y = 1*block_size + block_size/2, n_texture = random.randint(1, 4)))
		self.prop_list.append(Tree(starting_x = 7*block_size + block_size/2, starting_y = 5*block_size + block_size/2, n_texture = random.randint(1, 4)))
		self.prop_list.append(Tree(starting_x = 7*block_size + block_size/2, starting_y = 4*block_size + block_size/2, n_texture = random.randint(1, 4)))
		self.prop_list.append(Tree(starting_x = 7*block_size + block_size/2, starting_y = 3*block_size + block_size/2, n_texture = random.randint(1, 4)))
		self.enemy_list.append(Archer(starting_x = 0*block_size + block_size/2, starting_y = 5*block_size + block_size/2))
		self.enemy_list.append(Archer(starting_x = 4*block_size + block_size/2, starting_y = 4*block_size + block_size/2))
		self.enemy_list.append(Archer(starting_x = 4*block_size + block_size/2, starting_y = 1*block_size + block_size/2, rotation = 180))
		self.enemy_list.append(Archer(starting_x = 7*block_size + block_size/2, starting_y = 7*block_size + block_size/2, rotation = 180))
		self.enemy_list.append(Knight(starting_x = 0*block_size + block_size/2, starting_y = 3*block_size + block_size/2))
		self.enemy_list.append(Knight(starting_x = 2*block_size + block_size/2, starting_y = 7*block_size + block_size/2, rotation = 180))
		self.enemy_list.append(Knight(starting_x = 4*block_size + block_size/2, starting_y = 2*block_size + block_size/2, rotation = 180))
		self.enemy_list.append(Knight(starting_x = 7*block_size + block_size/2, starting_y = 6*block_size + block_size/2, rotation = 180))
		self.enemy_list.append(Knight(starting_x = 7*block_size + block_size/2, starting_y = 1*block_size + block_size/2, rotation = 180))


	def on_draw(self):
		arcade.start_render()  #always first

		#draw all the sprites
		self.tile_list.draw()
		self.slime_list.draw()
		self.prop_list.draw()
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

		#print(self.slime_list[0].center_x, self.slime_list[0].center_y)

	def on_key_release(self, key, modifiers):  #optional
		pass

	def update(self, delta_time):
		self.slime_list.update()

		#Tree Power up
		for i in range(len(self.prop_list)):
			if(self.prop_list[i].inrange(self.slime_list[0]) and self.slime_list[0].cur_health == 1):
				print("You have obtained tree armor and you are hidden against the Archer's attack.")
				self.slime_list[0].cur_health += 1

		#fire if in range
		for i in range(len(self.enemy_list)):
			if(self.enemy_list[i].inrange(self.slime_list[0]) or self.enemy_list[i].current_texture > 0):
				self.enemy_list[i].change_texture()
				#print("texture", self.enemy_list[i].current_texture)

			if(self.enemy_list[i].killed):
				self.slime_list[0].cur_health -= 1
				self.enemy_list[i].killed = False
				#print("health", self.slime_list[0].cur_health)
				if(self.slime_list[0].cur_health == 0):
					print("Game Over")
					exit()

		#stop slime movement
		if((self.slime_list[0].change_x > 0 and self.slime_list[0].center_x >= self.next_x) or (self.slime_list[0].change_x < 0 and self.slime_list[0].center_x <= self.next_x)):
			self.slime_list[0].change_x = 0
			self.slime_list[0].center_x = self.next_x
		if((self.slime_list[0].change_y > 0 and self.slime_list[0].center_y >= self.next_y) or (self.slime_list[0].change_y < 0 and self.slime_list[0].center_y <= self.next_y)):
			self.slime_list[0].change_y = 0
			self.slime_list[0].center_y = self.next_y

		player_collision_list = arcade.check_for_collision_with_list(self.slime_list[0], self.enemy_list)

		#Game Over
		for collision in player_collision_list:
			self.slime_list[0].cur_health -= 1
			if(self.slime_list[0].cur_health == 0):
				print("Game Over")
				exit()

		if(self.slime_list[0].center_x == 6*block_size + block_size/2 and self.slime_list[0].center_y == 0*block_size + block_size/2):
			print("Congratulations!\nYou have passed the level.")
			exit()


#initialise game
game = MyGame(screen_width, screen_height, "Slime Adventures")
game.setup()
arcade.run()