class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def fractional_knapsack(capacity, items):
    # Sort items by their value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0.0
    knapsack = []

    for item in items:
        if capacity == 0:
            break
        if item.weight <= capacity:
            # Take the whole item
            capacity -= item.weight
            total_value += item.value
            knapsack.append((item.value, item.weight))
        else:
            # Take a fraction of the item
            fraction = capacity / item.weight
            total_value += item.value * fraction
            knapsack.append((item.value * fraction, capacity))
            capacity = 0

    return total_value, knapsack

# Example usage
items = [
    Item(60, 10),
    Item(100, 20),
    Item(120, 30)
]
capacity = 50

max_value, knapsack = fractional_knapsack(capacity, items)
print(f"Maximum value: {max_value}")
print("Knapsack contents:")
for value, weight in knapsack:
    print(f"Value: {value}, Weight: {weight}")
