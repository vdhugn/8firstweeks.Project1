num = int(input())

def old_lv(n):
    if n <= 50 :
        price = n * 1728
    elif 50 < n <= 100:
        price = 50 * 1728 + (n - 50) * 1786
    elif 100 < n <= 200:
        price = 50 * 1728 + 50 * 1786 + (n - 100) * 2074
    elif 200 < n <= 300:
        price = 50 * 1728 + 50 * 1786 + 100 * 2074 + (n - 200) * 2612
    elif 300 < n <= 400:
        price = 50 * 1728 + 50 * 1786 + 100 * 2074 + 100 * 2612 + (n - 300) * 2919
    else:
        price = 50 * 1728 + 50 * 1786 + 100 * 2074 + 100 * 2612 + 100 * 2919 + (n - 400) * 3015
    return (price * 1.1)

def new_lv(n):
    if n <= 100 :
        price = n * 1728
    elif 100 < n <= 200:
        price = 100 * 1728 + (n - 100) * 2074
    elif 200 < n <= 400:
        price = 100 * 1728 + 100 * 2074 + (n - 200) * 2612
    elif 400 < n <= 700:
        price = 100 * 1728 + 100 * 2074 + 200 * 2612 + (n - 400) * 3111
    else:
        price = 100 * 1728 + 100 * 2074 + 200 * 2612 + 300 * 3111 + (n-700) * 3457
    return (price * 1.1)

def main():
    res = new_lv(num) - old_lv(num)
    print('{0:.{1}f}'.format(res, 2))

main()