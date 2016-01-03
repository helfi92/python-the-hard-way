from sys import exit
from random import randint


class Scene(object):
	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()"
			exit(1)

class Engine(object):
	def __init__(self,scene_map):
		self.scene_map = scene_map
	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print "\n----------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
	quips = [
		"You died. You kinda suck at this.",
		"Your mom would be proud... if she were smarter.",
		"Such a luser",
		"I have a small puppy that's better at this."

	]
	def enter(self):
		print Death.quips[randint(0,len(self.quips)-1)]

class CentralCorridor(Scene):
	def enter(self):
		print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
		print "your entire crew. You are the last surviving member and our last"
		print "mission is to get the neutron destruct bomb from the Weapons Armory,"
		print "put it in the bridge, and blow the ship up after getting into an "
		print "escape pod."
		print "\n"
		print "Youre running down the central corridor to the Weapons Armory when"
		print "a Gothon jumps out, red scaly skin, dark grimy teeth, and eil clown costume"
		print "flowing around his hate filled body. He's blocking the door to the "
		print "Armory and about to pull a weapon to blast you."

		action = raw_input("> ")

		if action == "shoot!":
			print "You are dead"
			return 'death'
		elif action == "dodge!":
			print "You are dead"
			return 'death'
		elif action == "tell a joke":
			print "While he's laughing, you kill him"
			return 'laser_weapon_armory'
		else:
			print "DOES NOT COMPUTE!"
			return 'cemtral_corridor'
		

class LaserWeaponArmory(Scene):
	def enter(self):
		pass

class TheBridge(Scene):
	def enter(self):
		pass

class EscapePod(Scene):
	def enter(self):
		pass

class Map(object):
	def __init__(self, start_scene):
		pass

	def next_scene(self, scene_name):
		pass
	def opening_scene(self):
		pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()