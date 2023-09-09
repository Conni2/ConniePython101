#dollar change calculator
def calculate_change():
    
    payment = int(input ("Money Received:"))
    cost = int(input ("Product Price:"))

    change = payment - cost

    hundred_count = change // 100 
    fifty_count = (change % 100) // 50 
    twenty_count = (change % 50) // 20
    ten_count = (change % 20) // 10
    five_count = (change % 10) // 5
    two_count = (change % 5) // 2
    one_count = (change % 2) // 1
    
    
    print("$100: {}ea".format(hundred_count))
    print("$50: {}ea".format(fifty_count))
    print("$20: {}ea".format(twenty_count))
    print("$10: {}ea".format(ten_count))
    print("$5: {}ea".format(five_count))
    print("$2: {}ea".format(two_count))
    print("$1: {}ea".format(one_count))
   


# Test
calculate_change()