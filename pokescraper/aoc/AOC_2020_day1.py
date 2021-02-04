def day1():
  f = open("day1_input", "r")
  numbers_arr = map(lambda num: int(num), f.read().split('\n'))
  as_ints = list(numbers_arr)
  number_set = set(as_ints);
  for n in as_ints:
    comp = 2020 - n
    if comp in number_set:
      print(n * (2020 - n))
      break





def day2_part1():
  valid_lines = 0;
  f = open("day2_input", "r")
  for line in f:
    min_value, max_value, letter, password = parseLine(line)
    times_letter_found = password.count(letter)
    if min_value <= times_letter_found <= max_value:
      print(line)
      valid_lines += 1

  print(f'Valid Lines: {valid_lines}')

def day2_part2():
  valid_lines = 0;
  f = open("day2_input", "r")
  for line in f:
    min_index, max_index, letter, password = parseLine(line)
    if password[min_index-1]==letter and password[max_index-1]!=letter or password[min_index-1]!=letter and password[max_index-1]==letter:
      print(line)
      valid_lines += 1

  print(f'Valid Lines: {valid_lines}')


def parseLine(line):
  parts = line.split(' ')
  min_max = parts[0].split('-')
  min_value = min_max[0];
  max_value = min_max[1];
  letter = parts[1][0]
  password = parts[2].replace('\n', '')

  return int(min_value), int(max_value), letter, password




def day3():
  valid_lines = 0;
  f = open("day3_input", "r")
  for line in f:
    min_index, max_index, letter, password = parseLine(line)
    if password[min_index-1]==letter and password[max_index-1]!=letter or password[min_index-1]!=letter and password[max_index-1]==letter:
      print(line)
      valid_lines += 1

  print(f'Valid Lines: {valid_lines}')

day1()
day2_part1()
day2_part2()
