#!/usr/bin/python

# Created by
#  Aaron Delaney - @devoxel - devoxel.net
# Created for CPSSD First Year Practicium
# All Right Reserved

import sys

class Shop(object):
    """ The shop class is responable for calculating shop prices and discounts

     As a user of this class, just call shop_instance.add_to_cart(item_name)
     until your cart is ready, then call checkout().

     shop_instance.checkout() returns three strings:
      - the total bill before deductions are applied
      - the total deduction amount
      - the final bill after deductions have been applied
    """
    def __init__(self):
        self.prices = {
            "plant":            7.00,
            "garden pot":       10.00,
            "small paint can":  9.95,
            "large paint can":  34.50,
            "paint brush":      6.95,
            "picture frame":    7.99,
            "lampshade":        30.00,
            "sandpaper":        .55,
            "box of screws":    2.5,
        }
        self.cart = {} # {item: quantity, item:quantity, ...}
        self.gardening_products = ("plant", "garden pot")
        self.paint_products = ("small paint can", "large paint can")

    def add_to_cart(self, item_name, quantity):
        """Add item to cart, quantity is strictly a positive integer"""
        try:
            if item_name in self.cart:
                self.cart[item_name] += quantity
            else:
                self.cart[item_name] = quantity
        except:
            print "Oops, something went wrong picking that item :("

    def checkout(self):
        total = self._get_cart_total()

        non_block_discount_total = 0
        deduction = 0

        for item in self.cart:
            item_price = self.prices[item]
            item_quantity = self.cart[item]
            if item in self.gardening_products:
                non_block_discount_total += item_price * item_quantity
                deduction += item_price * .25 * item_quantity
            elif item in self.paint_products:
                non_block_discount_total += item_price * item_quantity
                deduction += item_price * .5 * item_quantity

        total_to_deduct = total - non_block_discount_total
        if total < 50:
            deduction += total_to_deduct * .05
        elif total < 100:
            deduction += total_to_deduct * .075
        elif total < 250:
            deduction += total_to_deduct * .10
        else:
            deduction += total_to_deduct * .15

        print "# Total bill before deductions:", total
        print "# Total deductions:", deduction
        print "# Final bill: ", total - deduction

    def _get_cart_total(self):
        total = 0
        for item in self.cart:
            item_price = self.prices[item]
            item_quantity = self.cart[item]
            total += item_price * item_quantity
        return total

    def list_items(self):
        return self.prices.keys()

    def __str__(self):
        output =  "\n"
        output += "# Current Cart: \n"
        for item in self.cart:
            quantity = self.cart[item]
            price = self.prices[item]
            output += "# " + str(quantity) + 'x ' + item
            output += " @ " + str(price) + 'EUR'
            output += '\n\ttotal value ex. deductions: ' + str(price*quantity)
            output += ' EUR\n'
        return output

def get_items_to_add(shop_instance, menu):
    running = True
    items = shop_instance.list_items()

    product_list = "#-1: back \n"
    for product in items:
        product_list += '# ' + str(items.index(product)) + ': ' + product + '\n'

    while True:
        print "\n# Enter a number to choose the corresponding item   #"
        print product_list
        user_task = raw_input("$: ")

        try:
            if int(user_task) == -1:
                break
            chosen_item = items[int(user_task)]
            quantity = abs(int(raw_input("# quantity: ")))
            shop_instance.add_to_cart(chosen_item, quantity)
        except ValueError:
            print "# invalid item or quantity, -1 to exit"
        except IndexError:
            print "# invalid item, -1 to exit"
        except KeyError:
            print "# invalid item, -1 to exit"

    print menu # to avoid confusion upon re-entering main menu
    return True

def checkout_cart(shop_instance, menu):
    shop_instance.checkout()
    return True

def print_cart(shop_instance, menu):
    print shop_instance
    return True

def print_help(shop_instance, menu):
    print menu
    return True

def exit_cart(shop_instance, menu):
    return False

def main():
    """This function is responable for handling user input and the main loop"""
    # To make this program less verbose I decided not to have a dedicated
    # output manager, so all text is handled naivly and is handwritten

    # this is the easiest way to make multiline strings look good, since
    # using docstrings creates tabbing issues
    menu =  "# Enter a number to choose the corresponding action #\n" + \
            "#  1: Add items to cart                             #\n" + \
            "#  2: Checkout                                      #\n" + \
            "#  3: See current cart                              #\n" + \
            "#  4: Print help                                    #\n" + \
            "#  5: Leave shop                                    #"

    tasks = {
        1: get_items_to_add,
        2: checkout_cart,
        3: print_cart,
        4: print_help,
        5: exit_cart,
    }

    print menu
    running = True
    shop_instance = Shop()

    while running:
        user_task = raw_input("$: ")

        try:
            user_task = int(user_task)
            running = tasks[user_task](shop_instance, menu)
        except ValueError:
            print '# 4 for help, 5 to exit'


welcome = """
 ______   ___   ___ ___  __  _____      _____ ______   ___   ____     ___
|      | /   \ |   |   ||  |/ ___/     / ___/|      | /   \ |    \   /  _]
|      ||     || _   _ ||_ (   \_     (   \_ |      ||     ||  D  ) /  [_
|_|  |_||  O  ||  \_/  |  \|\__  |     \__  ||_|  |_||  O  ||    / |    _]
  |  |  |     ||   |   |    /  \ |     /  \ |  |  |  |     ||    \ |   [_
  |  |  |     ||   |   |    \    |     \    |  |  |  |     ||  .  \|     |
  |__|   \___/ |___|___|     \___|      \___|  |__|   \___/ |__|\_||_____|
"""

if __name__ == '__main__':
    print welcome

    arguments = sys.argv # no reason to use argparse when we're only using 1 arg
    test = False

    if len(arguments) > 1:
        if arguments[1] == '--test':
            test = True

    if test:
        print '# Entering test suite\n'
        # Reminder of keys:
        # "plant":            7.00,
        # "garden pot":       10.00,
        # "small paint can":  9.95,
        # "large paint can":  34.50,
        # "paint brush":      6.95,
        # "picture frame":    7.99,
        # "lampshade":        30.00,
        # "sandpaper":        .55,
        # "box of screws":    2.5,
        shop1 = Shop()
        shop1.add_to_cart('lampshade', 3)
        shop1.add_to_cart('small paint can', 2)
        shop1.checkout()
        print '\tExpected: Before: 109.90 | After 90.95'
        shop2 = Shop()
        shop2.add_to_cart('plant', 5)
        shop2.add_to_cart('picture frame', 30)
        shop2.checkout()
        print '\tExpected: Before: 274.70 | After 229.995'
        shop3 = Shop()
        shop3.add_to_cart('lampshade', 2)
        shop3.add_to_cart('paint brush', 4)
        shop3.add_to_cart('sandpaper', 5)
        shop3.add_to_cart('box of screws', 3)
        shop3.checkout()
        print '\tExpected: Before: 98.05 | After 90.70'

    else:
        main()
