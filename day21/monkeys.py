file1 = open('input.txt', 'r')
lines = file1.readlines()
stripped = [line.strip() for line in lines]

class Monkey:
    def __init__(self, name, value, operand, left_name, right_name, left_monkey, right_monkey):
        self.name = name
        self.value = value
        self.operand = operand
        self.left_name = left_name
        self.right_name = right_name
        self.left_monkey = left_monkey
        self.right_monkey = right_monkey
        self.evaluated = (value != None)

    def __str__(self):
        return f"""{self.name}, {self.value}, {self.left_name} {self.operand} {self.right_name}"""

    def evaluate_monkey(self):
        # Monkey is a leaf and/or already has value
        if self.evaluated:
            return self.value

        # Calculate left and right monkey values before proceeding
        self.left_monkey.evaluate_monkey()
        self.right_monkey.evaluate_monkey()
        
        # Monkey has both values needed to calculate its own value
        if self.operand == "+":
            self.value = self.left_monkey.value + self.right_monkey.value
        if self.operand == "-":
            self.value = self.left_monkey.value - self.right_monkey.value
        if self.operand == "*":
            self.value = self.left_monkey.value * self.right_monkey.value
        if self.operand == "/":
            self.value = self.left_monkey.value / self.right_monkey.value
        
        self.evaluated = True
    
        return self.value

    def contains_human(self):
        if self.name == "humn":
            return True
            
        left_has_human = False
        right_has_human = False
        if self.left_monkey != None:
            left_has_human = self.left_monkey.contains_human()
        if self.right_monkey != None:
            right_has_human = self.right_monkey.contains_human()

        return left_has_human or right_has_human

def parse_monkey(line):
    split = line.split(" ")
    name = split[0].replace(':', '')

    if len(split) == 2:
        return Monkey(name, int(split[1]), None, None, None, None, None)
    else:
        return Monkey(name, None, split[2], split[1], split[3], None, None)

def build_monkey_tree(stripped, human_value = None):
    monkey_table = {}
    for line in stripped:
        if len(line) == 0:
            break

        monkey = parse_monkey(line)
        monkey_table[monkey.name] = monkey

    if human_value != None:
        monkey_table["humn"].value = human_value

    for key in monkey_table.keys():    
        top_monkey = monkey_table[key]
        if top_monkey.value != None:
            continue

        top_monkey.left_monkey = monkey_table[top_monkey.left_name]
        top_monkey.right_monkey = monkey_table[top_monkey.right_name]

    return monkey_table["root"]

def get_left_monkey_val(stripped, human_value = None):
    root = build_monkey_tree(stripped, human_value)
    return root.left_monkey.evaluate_monkey()

# Gimme that number, monkey
root = build_monkey_tree(stripped)
print(root.evaluate_monkey())

# Left tree has the human, so that's the one to mess around with, while keeping
# the right monkey's value as the target
print("left has human", root.left_monkey.contains_human())
print("right has human", root.right_monkey.contains_human())

target = root.right_monkey.value
print("target for left", target)

# An increase in the human value decreases the value of the left tree. Casting our net
# wide, we can start with a minimum and max value that encapsulate our target 
minimum = -10e5
maximum = 10e15
print(get_left_monkey_val(stripped, minimum))
print(get_left_monkey_val(stripped, maximum))

# Now start looking via binary search for an integer that will get us to the target
delta = 0.05
iterations = 0
max_iterations = 100000
current = (minimum + maximum) / 2

while True:
    current = (minimum + maximum) / 2
    current_val = get_left_monkey_val(stripped, current)

    if abs(get_left_monkey_val(stripped, current) - target) < delta:
        break

    if iterations == max_iterations:
        print("max iterations hit")
        break

    if current_val > target:
        minimum = current
    else:
        maximum = current
    
    iterations += 1

print(current)
print(get_left_monkey_val(stripped, current))
