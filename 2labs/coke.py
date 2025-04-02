def main():
    coins = ["5", "10", "25"]
    price = 50
    inserted = 0

    while inserted < price:
        print(f"Amount Due: {price - inserted}")
        coin = input("Insert Coin: ")
        if coin in coins:
            inserted += int(coin)

    print(f"Change Owed: {inserted - price}")



main()