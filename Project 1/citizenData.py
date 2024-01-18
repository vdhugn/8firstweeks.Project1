from datetime import datetime

def is_valid_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        # Additional check for out-of-range day values
        return 1 <= date_obj.day <= 31
    except ValueError:
        return False

def parse_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d')

def number_people(database):
    return len(database)

def number_people_born_at(database, date):
    target_date = parse_date(date)
    if not is_valid_date(date):
        return 0
    return sum(1 for entry in database if parse_date(entry[1]) == target_date)

def most_alive_ancestor(database, code):
    def find_ancestor(curr_code, generation):
        if curr_code == "0000000":
            return (generation, curr_code)

        person = next(entry for entry in database if entry[0] == curr_code)
        father_gen, _ = find_ancestor(person[2], generation + 1)
        mother_gen, _ = find_ancestor(person[3], generation + 1)

        return max(father_gen, mother_gen), curr_code
    generation, ancestor_code = find_ancestor(code, 0)
    return generation - 1

def number_people_born_between(database, from_date, to_date):
    from_date1 = parse_date(from_date)
    to_date1 = parse_date(to_date)
    if not is_valid_date(from_date) or not is_valid_date(to_date):
        return 0
    return sum(1 for entry in database if from_date1 <= parse_date(entry[1]) <= to_date1)

def max_unrelated_people(database):
    # Create sets for all people and related people
    all_people = set(entry[0] for entry in database)
    related_people = set(entry[2] for entry in database if entry[2] != "0000000")
    related_people.update(entry[3] for entry in database if entry[3] != "0000000")

    # Find the maximal subset of unrelated people
    unrelated_people = all_people - related_people
    max_unrelated_size = 0
    current_subset_size = 0

    for person in unrelated_people:
        current_subset_size += 1
        if current_subset_size > max_unrelated_size:
            max_unrelated_size = current_subset_size

    return max_unrelated_size

# Read the database
database = []
while True:
    line = input().strip()
    if line == '*':
        break
    data = line.split()
    database.append(data)

# Process queries
result = []
while True:
    query = input().strip()
    if query == '***':
        break
    if query == 'NUMBER_PEOPLE':
        result.append(number_people(database))
    elif query.startswith('NUMBER_PEOPLE_BORN_AT'):
        _, date = query.split()
        result.append(number_people_born_at(database, date))
    elif query.startswith('MOST_ALIVE_ANCESTOR'):
        _, code = query.split()
        result.append(most_alive_ancestor(database, code))
    elif query.startswith('NUMBER_PEOPLE_BORN_BETWEEN'):
        _, from_date, to_date = query.split()
        result.append(number_people_born_between(database, from_date, to_date))
    elif query == 'MAX_UNRELATED_PEOPLE':
        result.append(max_unrelated_people(database))

for i in result:
    print(i)
