hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

if hours > 40:
    gross_pay = 40 * rate + (hours - 40) * (rate * 1.5)
else:
    gross_pay = hours * rate

print(f"Gross pay: ${gross_pay:.2f}")