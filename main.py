import math as m

def FormatPhoneNumber(phone):
    return "Your Formatted Phone Number: ({0}) {1}-{2}".format(phone[0:3], phone[3:6], phone[6:])

def main():
    number = input("Enter 10 Digit Phone Number(e.g 1234567890)")

    print(FormatPhoneNumber(number))

main()