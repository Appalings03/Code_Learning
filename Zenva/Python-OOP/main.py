# 2. Intro to Repl.it
print("Hello world!")

# 3. Numbers and booleans
position = 27
pi = 3.14
is_game_over = False
print(position)
print(type(position))

# 4. Strings
hello_text = "Hello world!"
name = 'Nimish'
print(hello_text)
print(len(name))

# 5. Arithmetic and assignment operators
# Operators: = + - * / % // **
position = 5
forwards = position + 1
backwards = position - 1
position += 1
print(position)

# 6. Comparison operators and logical
# Operators: > >= < <= == != not or and
is_at_end = position == 10
is_past_halfway = position >= 5
is_game_over = not is_game_over
points = 10
is_game_over = points >= 10 and is_at_end
print(is_game_over)

# 7. Lists
enemy_positions = [5, 10, 15]
first_position = enemy_positions[0]
enemy_positions[1] = 12
enemy_positions.append(20)
del(enemy_positions[1])
print(len(enemy_positions))
print(enemy_positions)

# 8. Tuples
high_score = ("Nimish", 100)
high_score = ("Holly", 120)
print(len(high_score))

# 9. Dictionaries
actions = {"r": 1, "l": -1}
right = actions["r"]
actions["u"] = 1
print(actions)

# 10. If statements
action = "r"
if action == "r":
  print("Move right")
elif action == "l":
  print("Move left")
else:
  print("Invalid key")

# 11. While loops
position = 0
end_position = 5
while position < end_position:
  print(position)
  position += 1
print("You've reached the end!")

# 12. For in loops
for action in actions:
  print(action)

# 13. Functions
position = 0
def move_player():
  global position
  position += 1
move_player()
print(position)

# 14. Function parameters
def move_player(by_amount):
  global position
  position += by_amount
move_player(5)
print(position)

# 15. Return values
def move_player(position, by_amount):
  return position + by_amount
position = move_player(0, 5)

# 16. Intro to classes and objects
class GameObject:

  def __init__(self, name, x_pos, y_pos):
    self.name = name
    self.x_pos = x_pos
    self.y_pos = y_pos

  def move(self, by_x_amount, by_y_amount):
    self.x_pos += by_x_amount
    self.y_pos += by_y_amount

game_object = GameObject("Enemy", 1, 2)
game_object.move(5, 6)
print(game_object.name)

# 17. Inheritance:
class Enemy(GameObject):

  def __init__(self, name, x_pos, y_pos, health):
    super().__init__(name, x_pos, y_pos)
    self.health = health

  def take_damage(self, amount):
    self.health -= amount
    if self.health < 0:
      return

enemy = Enemy("Enemy 1", 5, 10, 100)
enemy.take_damage(20)
print(enemy.health)