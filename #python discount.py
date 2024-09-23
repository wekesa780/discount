total_amount = float(input("Enter total amount: "))

if total_amount >= 1000 and total_amount < 5000:  # 10% discount
    discount = total_amount * 0.1
    amount_to_pay = total_amount - discount
    print(f"The discount is: {discount} and amount to pay: {amount_to_pay}")
elif total_amount >= 5000:  # 20% discount
    discount = total_amount * 0.2
    amount_to_pay = total_amount - discount
    print(f"The discount is: {discount} and amount to pay: {amount_to_pay}")
else:  # No discount
    discount = 0
    amount_to_pay = total_amount
    print(f"No discount. Amount to pay: {amount_to_pay}")

    