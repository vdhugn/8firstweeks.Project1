def input_sequence_and_queries():
    sequence = []
    queries = []

    while True:
        line = input()
        if line == "*":
            break

        sequence.append(int(line))

    while True:
        line = input()
        if line == "***":
            break

        queries.append(line)

    return sequence, queries

sequence, queries = input_sequence_and_queries()