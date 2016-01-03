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
		print "You do a dive roll into the Weapon Armory, crouch and scan the room"
		print "for more Gothons that might be hiding"
		print "the code of the bomb is 3 digits"
		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9) )
		guess = raw_input("[keypad]> ")
		guesses = 0

		while guess != code and guesses < 10:
			print "BZZZZEDDD!"
			guesses +=1
			guess = raw_input("keypad]> ")

			if guess == code:
				print "The container clicks open and the seal breaks, letting gas out."
				print "You grab the neutron bomb and run as fast as you can to the"
				print "bridge where you must place it in the right spot."
				return 'death'
			else:
				print 'oups, you die'
				return 'death'


class TheBridge(Scene):
	def enter(self):
		print "You burst onto the Bridge with the neutron destruct bomb"
		print "under your arm and surprise 5 Gothons who are trying to"
		print "take control of the ship. Each of them has an even uglier"
		print "clown costume than the last. They haven't pulled their"
		print "weapons out yet, as they see the active bomb under your"
		print "arm and don't want to set it off."

		action = raw_input("> ")

		if action == "throw the bomb":
			print "you die"
			return 'death'
		elif action == "slowly place the bomb":
			print "Now that the bomb is placed you run to the escape pod to"
			print "get off this tin can."
			return 'escape_pod'
		else:
			print "DOES NOT COMPUTE"
			return "the_bridge"	

class EscapePod(Scene):
	def enter(self):
		print "You rush through the ship desperately trying to make it to"
		print "the escape pod before the whole ship explodes"
		print "bout you don't have time to look. There's 5 pods, which one do you take?"

		good_pod = randint(1,5)
		guess = raw_input("[ipod #]> ")

		if int(guess) != good_pod:
			print "you jump into your own death"
			return 'death'
		else:
			print "Fantastic! you are done your mission"
			return 'finished'


class Map(object):
	
	scenes = {
		'central_corridor' : CentralCorridor(),
		'laser_weapon_armory' : LaserWeaponArmory(),
		'the_bridge' : TheBridge(),
		'escape_pod' : EscapePod(),
		'death' : Death()
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)
	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()