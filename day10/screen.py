file1 = open('input.txt', 'r')
lines = file1.readlines()
stripped = [line.strip() for line in lines]

class GraphScreen:
    def __init__(self, start_signal, start_cycle):
        self.current_signal = start_signal
        self.cycle = start_cycle
        self.signal_totals = []
        self.pixels = []
        self.width = 40
        self.height = 6

        for i in range(self.height):
            self.pixels.append([])

        self.add_pixel()

    def clock_cycle(self):
        self.add_pixel()
        self.cycle += 1

    def execute_command(self, line):
        self.signal_check()
        self.clock_cycle()

        cmd = line.split()
        if cmd[0] == "noop":
            return
        
        self.signal_check()
        to_add = int(cmd[1])
        self.current_signal += to_add
        self.clock_cycle()

    def signal_check(self):
        if self.cycle % self.width == 20:
            self.signal_totals.append(self.cycle * self.current_signal)

    def add_pixel(self):
        pixel_row_idx = int(self.cycle / self.width)
        if pixel_row_idx >= self.height:
            return

        current_screen_row = self.pixels[pixel_row_idx]
        
        if self.is_pixel_lit():
            current_screen_row.append("#")
        else:
            current_screen_row.append(".")

    def is_pixel_lit(self):
        printer_head = self.cycle % self.width
        sprite_positions = [self.current_signal - 1, self.current_signal, self.current_signal + 1]
        return printer_head in sprite_positions

    def print_screen(self):
        for row in self.pixels:
            line = ""
            for pixel in row:
                line += pixel
            print(line)
                
    
screen = GraphScreen(1, 1)

for idx, line in enumerate(stripped):
    if len(line) == 0:
        break
    
    screen.execute_command(line)


print(screen.signal_totals)
print(sum(screen.signal_totals))

screen.print_screen()
