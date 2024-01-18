def database_operations(keys, actions):

  # Create a hash table to store the keys in the database.
  hash_table = {}
  for key in keys:
    hash_table[key] = 1

  # Perform the actions on the database.
  results = []
  for action in actions:
    cmd, key = action.split()

    if cmd == "find":
      result = 1 if key in hash_table else 0
    elif cmd == "insert":
      result = 1 if key not in hash_table else 0
      if result:
        hash_table[key] = 1
    results.append(result)
  return results

# Read the input data.
keys = []
while True:
  key = input()
  if key == "*":
    break
  keys.append(key)

actions = []
while True:
  action = input()
  if action == "***":
    break
  actions.append(action)

# Perform the database operations and print the results.
results = database_operations(keys, actions)
for result in results:
  print(result)