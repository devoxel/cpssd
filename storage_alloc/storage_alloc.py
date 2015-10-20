"""

usage: storage_alloc.py [path to location table] [path to item table]

# Location table format:
  location name; capacity; distance in meters;

# Item table format:
  item name; quantity; freq of checkouts per month;

"""

import sys

def main():
    location_path = sys.argv[1]
    item_path     = sys.argv[2]
    
    locations = open_file(location_path)
    items = open_file(item_path)
    allocations = allocate_storage(locations, items)
    
    print allocations
    while True:
        user_input = raw_input('Whats your item: ')
        print allocations[user_input]

def allocate_storage(locations, items):
    alloc = {}
    
    item_list = sorted(items, key=lambda key: items[key][1]/items[key][0], reverse=True)
    location_list = sorted(locations, key=lambda key: locations[key][1])
    
    for item in item_list:
        stored = 0
        quantity = items[item][0]
        freq = items[item][1]
        for location in location_list:
            capacity = locations[location][0]
            if capacity <= 0:
                continue
            distance = locations[location][1]
            if stored == quantity:
                break
            else:
                if capacity < (quantity - stored) :                    
                    storing_on_location = capacity                
                else:
                    storing_on_location = quantity - stored
                if item not in alloc:
                    alloc[item] = [(location, storing_on_location)]
                else:
                    alloc[item].append((location, storing_on_location))
                stored += storing_on_location
                locations[location][0] -= storing_on_location
    return alloc

def parse_line(s):
    l = s.rstrip('\n').split(';')  
    return [l[0], int(l[1]), int(l[2])]   

def open_file(path):
    table = {}
    with open(path) as f:
        for l in f:
            values = parse_line(l)
            table[values[0]] = values[1:]
    return table

if __name__ == "__main__":
    main()
