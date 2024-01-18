class Order:
    def __init__(self, customer_id, product_id, price, shop_id, time_point):
        self.customer_id = customer_id
        self.product_id = product_id
        self.price = price
        self.shop_id = shop_id
        self.time_point = time_point

def read_operational_data():
    orders = []
    while True:
        line = input()
        if line == '#':
            break
        parts = line.split(' ')
        customer_id = parts[0]
        product_id = parts[1]
        price = int(parts[2])
        shop_id = parts[3]
        time_point = parts[4]
        orders.append(Order(customer_id, product_id, price, shop_id, time_point))
    return orders

def total_number_orders(orders):
    return len(orders)

def total_revenue(orders):
    total_revenue = 0
    for order in orders:
        total_revenue += order.price
    return total_revenue

def revenue_of_shop(orders, shop_id):
    shop_revenue = 0
    for order in orders:
        if order.shop_id == shop_id:
            shop_revenue += order.price
    return shop_revenue

def total_consume_of_customer_shop(orders, customer_id, shop_id):
    customer_consume = 0
    for order in orders:
        if order.customer_id == customer_id and order.shop_id == shop_id:
            customer_consume += order.price
    return customer_consume

def total_revenue_in_period(orders, from_time, to_time):
    period_revenue = 0
    for order in orders:
        if order.time_point >= from_time and order.time_point <= to_time:
            period_revenue += order.price
    return period_revenue

def main():
    orders = read_operational_data()
    result = []
    while True:
        line = input()
        if line == '#':
            break

        parts = line.split(' ')
        query_type = parts[0]

        if query_type == '?total_number_orders':
            result.append(total_number_orders(orders))
            
        elif query_type == '?total_revenue':
            result.append(total_revenue(orders))
            
        elif query_type == '?revenue_of_shop':
            shop_id = parts[1]
            result.append(revenue_of_shop(orders, shop_id))
            
        elif query_type == '?total_consume_of_customer_shop':
            customer_id = parts[1]
            shop_id = parts[2]
            result.append(total_consume_of_customer_shop(orders, customer_id, shop_id))
            
        elif query_type == '?total_revenue_in_period':
            from_time = parts[1]
            to_time = parts[2]
            result.append(total_revenue_in_period(orders, from_time, to_time))
            
        else:
            result.append('Invalid query')

    return result

query_result = main()
for i in query_result:
    print(i)
