import csv

productsFile = open("products.csv")
products = csv.reader(productsFile)

catalog = []

for row in products:
    if len(row) > 0:
        id = row[0]
        name = row[1]
        price = float(row[2])
        targetQuantity = int(row[3])
        currentQuantity = int(row[4])
        catalog.append({"id": id, "name": name, "price": price, "quantity": {
            "target": targetQuantity, "current": currentQuantity}})


def view():
    print("\nReorder List\nid\t\tName\tCurrent Quantity\tTarget Quantity\tReorder Amount")

    for product in catalog:
        currentQuantity = product['quantity']['current']
        targetQuantity = product['quantity']['target']
        print(
            f"{product['id']}\t{product['name']}\t{currentQuantity}\t\t\t{targetQuantity}\t\t{targetQuantity - currentQuantity}")


def reorderStock():
    print("Placing orders...")

    file = open("products.csv", "w")
    writer = csv.writer(file)

    for product in catalog:
        targetQuantity = product["quantity"]["target"]

        writer.writerow([product["id"], product["name"],
                        product["price"], targetQuantity, targetQuantity])

    file.close()
    print("Orders placed, stock replenished")


menuChoice = input("1 - View stock levels\n2 - Reorder stock\n")

if menuChoice == "1":
    view()

elif menuChoice == "2":
    reorderStock()

else:
    print("Invalid option")

productsFile.close()
