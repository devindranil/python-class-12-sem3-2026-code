# shopping disocunt calculator

purchase=float(input("Enter total purchase shopping amount: "))
are_you_member=input("Are you a Member:? (Type Y or N): ")

if are_you_member=="Y":
    if purchase>=5000:
        discount=purchase*0.20 #20%
    else:
        discount=purchase*0.10 #10%
else:
    if purchase>=5000:
        discount=purchase*0.05 #5%
    else:
        discount=0

final_bill = purchase-discount

print("Purchase Amount: ",purchase)
print("Discount: ",discount)
print("Final Bill: ",final_bill)