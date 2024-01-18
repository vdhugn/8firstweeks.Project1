class Transaction:
    def __init__(self, from_account, to_account, money, time_point, atm):
        self.from_account = from_account
        self.to_account = to_account
        self.money = money
        self.time_point = time_point
        self.atm = atm

def read_transaction_data():
    transactions = []
    while True:
        line = input()
        if line == '#':
            break
        parts = line.split(' ')
        from_account = parts[0]
        to_account = parts[1]
        money = int(parts[2])
        time_point = parts[3]
        atm = parts[4]
        transactions.append(Transaction(from_account, to_account, money, time_point, atm))
    return transactions

def number_of_transactions(transactions):
    return len(transactions)

def total_money_transaction(transactions):
    total_money = 0
    for transaction in transactions:
        total_money += transaction.money
    return total_money

def list_sorted_accounts(transactions):
    accounts = set()
    for transaction in transactions:
        accounts.update([transaction.from_account, transaction.to_account])
    return sorted(accounts)

def total_money_transaction_from_account(transactions, account):
    total_money = 0
    for transaction in transactions:
        if transaction.from_account == account:
            total_money += transaction.money
    return total_money

def inspect_cycle(transactions, account, k):
    if k == 1:
        return 0
    accounts_visited = set()
    accounts_visited.add(account)
    def dfs(current_account):
        if current_account in accounts_visited:
            return 1

        accounts_visited.add(current_account)
        for transaction in transactions:
            if transaction.from_account == current_account:
                next_account = transaction.to_account
                if next_account == account:
                    return 0
                elif next_account not in accounts_visited:
                    if dfs(next_account):
                        return 0

        accounts_visited.remove(current_account)
        return 0
    return dfs(account)

def main():
    transactions = read_transaction_data()
    result = []
    while True:
        line = input()
        if line == '#':
            break

        parts = line.split(' ')
        query_type = parts[0]      

        if query_type == '?number_transactions':
            result.append(number_of_transactions(transactions))
 
        elif query_type == '?total_money_transaction':
            result.append(total_money_transaction(transactions))
            
        elif query_type == '?list_sorted_accounts':
            result.append(' '.join(list_sorted_accounts(transactions)))

        elif query_type == '?total_money_transaction_from':
            account = parts[1]
            result.append(total_money_transaction_from_account(transactions, account))
            
        elif query_type == '?inspect_cycle':
            account = parts[1]
            k = int(parts[2])
            result.append(inspect_cycle(transactions, account, k))
           
        else:
            result.append('Invalid query')
    return result

query_result = main()
for i in query_result:
    print(i)
