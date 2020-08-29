# Function to compute shipment
def compute_shipment(order, warehouses):
    output = {}
    for item, want in order.items():
        # Keep track of found quantity vs. desired quantity of each item
        found = 0
        remaining = want
        # Comb through warehouses and add-on to total, prioritizing cheaper warehouses
        for warehouse in warehouses:
            inventory = warehouse['inventory']
            name = warehouse['name']
            if item in inventory:
                just_found = min(remaining, inventory[item])
                found += just_found
                # Create dict of dicts as final output
                if name not in output:
                    output[name] = {}
                output[name][item] = just_found
                remaining -= just_found
                if remaining <= 0:
                    break
        # If we could not fulfill an item, return []
        if remaining > 0:
            return []
    # Convert warehouse<>item<>quantity dict to list by warehouse
    return [{k:v} for k, v in output.items()]

# Run Test cases
print('Begin testing compute_shipment function.')
print('--------------')
print('Test case 1:')
order = {'apple': 5, 'banana': 5, 'orange': 5}
warehouses = [{'name': 'owd', 'inventory': {'apple': 5, 'orange': 10}}, {'name': 'dm', 'inventory': {'banana': 5, 'orange': 10}}]
print('Order:', order)
print('Warehouses:', warehouses)
assert compute_shipment(order, warehouses) == [{'owd': {'apple': 5, 'orange': 5}}, {'dm': {'banana': 5}}], 'Failed'
print('Passed')

print('--------------')
print('Test case 2:')
order = {'apple': 1}
warehouses = [{'name': 'owd', 'inventory': {'apple': 1}}]
print('Order:', order)
print('Warehouses:', warehouses)
assert compute_shipment(order, warehouses) == [{'owd': {'apple': 1}}], 'Failed'
print('Passed')

print('--------------')
print('Test case 3:')
order = {'apple': 10}
warehouses = [{'name': 'owd', 'inventory': {'apple': 5}}, {'name': 'dm', 'inventory': {'apple': 5}}]
print('Order:', order)
print('Warehouses:', warehouses)
assert compute_shipment(order, warehouses) == [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}], 'Failed'
print('Passed')

print('--------------')
print('Test case 4:')
order = {'apple': 1}
warehouses = [{'name': 'owd', 'inventory': {'apple': 0}}]
print('Order:', order)
print('Warehouses:', warehouses)
assert compute_shipment(order, warehouses) == [], 'Failed'
print('Passed')

print('--------------')
print('Test case 5:')
order = {'apple': 2}
warehouses = [{'name': 'owd', 'inventory': {'apple': 1}}]
print('Order:', order)
print('Warehouses:', warehouses)
assert compute_shipment(order, warehouses) == [], 'Failed'
print('Passed')

print('--------------')
print('Test case 6:')
order = {'apple': 7, 'banana': 12}
warehouses = [{'name': 'abcde', 'inventory': {'apple': 4, 'banana': 13}}, {'name': '12345', 'inventory': {'apple': 17, 'banana': 1}}]
print('Order:', order)
print('Warehouses:', warehouses)
assert compute_shipment(order, warehouses) == [{'abcde': {'apple': 4, 'banana': 12}}, {'12345': {'apple': 3}}], 'Failed'
print('Passed')

print('--------------')
print('Test case 7:')
order = {'apple': 100, 'banana': 100, 'orange': 100}
warehouses = [{'name': 'owd', 'inventory': {'apple': 100, 'orange': 100}}]
print('Order:', order)
print('Warehouses:', warehouses)
assert compute_shipment(order, warehouses) == [], 'Failed'
print('Passed')

print('--------------')
print('Finished testing compute_shipment function. All test cases passed.')