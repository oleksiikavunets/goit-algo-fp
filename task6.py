items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    items = dict(sorted(items.items(), key=lambda i: i[1]["calories"] / i[1]["cost"], reverse=True))
    total_calories = 0
    total_cost = 0
    selected_items = []

    for name, item in items.items():
        if budget >= item['cost']:
            budget -= item['cost']
            total_calories += item['calories']
            total_cost += item['cost']
            selected_items.append(name)
    return total_calories, total_cost, selected_items


def dynamic_programming(items, budget):
    n = len(items)
    K = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    calories = [item['calories'] for item in items.values()]
    costs = [item['cost'] for item in items.values()]

    for i in range(n + 1):
        for w in range(budget + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif costs[i - 1] <= w:
                K[i][w] = max(calories[i - 1] + K[i - 1][w - costs[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    selected_items = []
    total_cost = 0

    items = list(sorted(items.items(), key=lambda i: i[1]["calories"], reverse=True))

    total_calories = K[n][budget]

    for i in range(n):
        item_name, item = items[i]

        if item['cost'] <= budget:
            selected_items.append(item_name)
            budget -= item['cost']
            total_cost += item['cost']

    return total_calories, total_cost, selected_items


budget = 150

total_calories, total_cost, selected_items = greedy_algorithm(items, budget)

print('Greedy Algorithm: ')
print(f'Total Calories: {total_calories}')
print(f'Total Cost:     {total_cost}')
print(f'Selected Items: {selected_items}')

total_calories, total_cost, selected_items = dynamic_programming(items, budget)

print('Dynamic Programming: ')
print(f'Total Calories: {total_calories}')
print(f'Total Cost:     {total_cost}')
print(f'Selected Items: {selected_items}')

# Greedy Algorithm:
# Total Calories: 1120
# Total Cost:     120
# Selected Items: ['cola', 'potato', 'pepsi', 'hot-dog', 'hamburger']
#
# Dynamic Programming:
# Total Calories: 1220
# Total Cost:     140
# Selected Items: ['potato', 'pizza', 'hamburger', 'cola', 'pepsi']
