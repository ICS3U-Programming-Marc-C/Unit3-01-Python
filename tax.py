#!/usr/bin/env python3
# Created by Marc Coffi
# Created in March 2022
# This is a program that calculates the total cost using the HST of Nova Scotia

import constants


def main():
    # this function calculates total from subtotal and tax
    print("Hello! This program calculates the HST for Nova Scotia.")

    # input
    sub_total = float(input("Enter the subtotal: $"))

    # process
    tax = sub_total * constants.HST
    total = sub_total + tax

    # output
    print("")
    print("The HST is ${0:,.2f}".format(tax))
    print("The total cost is: ${0:,.2f}".format(total))


if __name__ == "__main__":
    main()
