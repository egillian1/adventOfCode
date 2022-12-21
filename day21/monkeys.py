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
        print(self.left_monkey, self.right_monkey)
        self.left_monkey.evaluate_monkey()
        self.right_monkey.evaluate_monkey()
        print(self.left_monkey, self.right_monkey)
        
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

def parse_monkey(line):
    split = line.split(" ")
    name = split[0].replace(':', '')

    if len(split) == 2:
        return Monkey(name, int(split[1]), None, None, None, None, None)
    else:
        return Monkey(name, None, split[2], split[1], split[3], None, None)

monkey_table = {}
for line in stripped:
    if len(line) == 0:
        break

    monkey = parse_monkey(line)
    monkey_table[monkey.name] = monkey


for key in monkey_table.keys():    
    top_monkey = monkey_table[key]
    print(top_monkey)
    if top_monkey.value != None:
        continue

    top_monkey.left_monkey = monkey_table[top_monkey.left_name]
    top_monkey.right_monkey = monkey_table[top_monkey.right_name]
    print(top_monkey)

print(monkey_table["root"].evaluate_monkey())
