import csv

productsFile = open("products.csv")
products = csv.reader(productsFile)

catalog = []

print("MY SHOP PRODUCTS")
for row in products:
    if len(row) > 0:
        id = row[0]
        name = row[1]
        price = float(row[2])

        catalog.append({"id": id, "name": name, "price": price})

        print(f"\n{name}\nid = {id} \nprice = {price}")


def convertToInt(i):
    try:
        return int(i)
    except ValueError:
        return None


orders = []


def printBasket():
    print("\n=====================================")
    print("Basket\n\nName\tQuantity\tPrice")

    total = 0

    for order in orders:
        price = order["quantity"] * order["price"]
        total += price
        print(
            f"{order['name']}\t{order['quantity']}\t\t{price}")

    print(f"\nTotal Price: {total}")
    print("=====================================")


while True:
    repeatText = "Do you want to order another product?"

    print("")
    productId = input("Enter the id of the product you want to order: ")

    product = next((i for i in catalog if i["id"] == productId), None)

    if product == None:
        print(f"Product with id {productId} not found")
        repeatText == "Do you want to try again?"
    else:
        print(product["name"])
        quantity = input("Quantity: ")
        quantity = convertToInt(quantity)

        if quantity == None:
            print("That's not a number")
            repeatText = "Do you want to try again?"
        else:
            order = next((i for i in orders if i["id"] == product["id"]), None)

            if (order == None):
                orders.append({**product, "quantity": quantity})
            else:
                idx = orders.index(order)
                orders[idx] = {**orders[idx],
                               "quantity": orders[idx]["quantity"] + quantity}

    printBasket()

    print("")
    repeat = input(f"{repeatText}\ny = yes\nn = no\n")
    if (repeat == "n"):
        printBasket()
        break

productsFile.close()
