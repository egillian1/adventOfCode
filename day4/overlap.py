file1 = open('input.txt', 'r')
lines = file1.readlines()
stripped = [line.strip() for line in lines]

def parse_line(line):
    ranges = line.split(",")
    first = ranges[0].split("-")
    second = ranges[1].split("-")

    first_range = {"start": int(first[0]), "end": int(first[1])}
    second_range = {"start": int(second[0]), "end": int(second[1])}

    return first_range, second_range

def contains_range(first, second):
    # First range is contained within second range
    if first["start"] >= second["start"] and first["end"] <= second["end"]:
        return True

    # Second range is contained withing first range
    if second["start"] >= first["start"] and second["end"] <= first["end"]:
        return True

    return False

def ranges_overlap(first, second):
    # First range is contained within second range
    if first["start"] >= second["start"] and first["start"] <= second["end"]:
        return True

    # Second range is contained withing first range
    if second["start"] >= first["start"] and second["start"] <= first["end"]:
        return True

    return False

ranges_contained = 0
overlaps = 0

for line in stripped:
    if len(line) == 0:
        break

    first_range, second_range = parse_line(line)

    if contains_range(first_range, second_range):
        ranges_contained += 1    

    if ranges_overlap(first_range, second_range):
        overlaps += 1

print(overlaps)
print(ranges_contained)
