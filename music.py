# Python musical keyboard simulator

keyboard_octave = ("C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B")

class Key:
	def __init__(self, button):
		try:
			self.button = int(button) % len(keyboard_octave)
			self.name = str(keyboard_octave[self.button])
		except:
			raise Exception("Invalid key.")
	
	def from_number(number):
		return Key(number % len(keyboard_octave))

	def from_name(name):
		return Key(keyboard_octave.index(name))

	def __str__(self):
		return str(self.name)

	def __int__(self):
		return int(keyboard_octave.index(self.name))

	def moveLeft(self):
		number = (int(self.button) - 1) % len(keyboard_octave)

		return Key(number)

	def moveRight(self):
		number = (int(self.button) + 1) % len(keyboard_octave)

		return Key(number)

	def sum(self, buttons = 1):
		r = self

		for i in range(0, buttons):
			r = r.moveRight()
		
		return r
	
	def subtract(self, buttons = 1):
		r = self

		for i in range(0, buttons):
			r = r.moveLeft()
		
		return r

class Chord:
	def order_keys(self):
		k1 = self.key1
		k2 = self.key2
		k3 = self.key3

		if k1.button > k2.button:
			k0 = k1
			k1 = k2
			k2 = k0

		if k1.button > k3.button:
			k0 = k1
			k1 = k3
			k3 = k0

		if k2.button > k3.button:
			k0 = k3
			k3 = k2
			k2 = k0
	
		self.key1 = k1
		self.key2 = k2
		self.key3 = k3

	def __init__(self, key1, key2, key3):
		self.key1 = Key(key1)
		self.key2 = Key(key2)
		self.key3 = Key(key3)

		if self.key1 == self.key2 or self.key1 == self.key3 or self.key2 == self.key3:
			raise Exception("Invalid chord.")

	def keys(self):
		return [self.key1, self.key2, self.key3]

	def moveLeft(self):
		newkey1 = self.key1.moveLeft()
		newkey2 = self.key2.moveLeft()
		newkey3 = self.key3.moveLeft()

		return Chord(newkey1, newkey2, newkey3)

	def moveRight(self):
		newkey1 = self.key1.moveRight()
		newkey2 = self.key2.moveRight()
		newkey3 = self.key3.moveRight()
	
		return Chord(newkey1, newkey2, newkey3)
  
	def __str__(self):
		self.order_keys()

		p1 = int(self.key1)
		p2 = int(self.key2)
		p3 = int(self.key3)

		if (p1, p2, p3) == (p1, p1 + 3, p1 + 7):
			return str(self.key1.name) + "m"
		elif (p1, p2, p3) == (p1, p1 + 4, p1 + 7):
			return str(self.key1.name)
		else:
			return "Unknown chord"
	
	def sum(self, buttons = 1):
		r = self

		for i in range(0, buttons):
			r = r.moveRight()
		
		return r
	
	def subtract(self, buttons = 1):
		r = self

		for i in range(0, buttons):
			r = r.moveLeft()
		
		return r

# Test in Python CLI

k1 = Key(1)
k2 = Key(5)
k3 = Key(8)

print(k1, "-", k2, "-", k3)

k2 = k2.subtract(1)

print(k1, "-", k2, "-", k3)

c1 = Chord(k1, k2, k3)

print(c1)

c2 = c1.sum(3)

print(c2)

c3 = Chord(k2, k1, k3)

print(c3)
