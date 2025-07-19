try:
    with open("Expectional Handling\Mini Project\items.txt", "r") as file:
        lines = file.readlines()

    total_items = len(lines)
    free_items = 0
    total_amount = 0

    for line in lines:
        name, price = line.strip().split(",")
        if price.strip() == "0":
            free_items += 1
        else:
            total_amount += float(price)

    discount = total_amount * 0.1
    final_amount = total_amount - discount

    print("Items Purchased:", total_items)
    print("Free Items:", free_items)
    print("Total Amount:", total_amount)
    print("Discount:", discount)
    print("Final Amount:", final_amount)

except FileNotFoundError:
    print("File not found.")
except ValueError:
    print("Invalid data format.")
except Exception as e:
    print("Error:", e)
