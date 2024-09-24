#python compound intrest calculator

# A = p(1+r/n)^t
# A=final amount
# p=initial principal balance
# r=intrest rate
# t=number of time periods elapsed

principle = 0
rate = 0
time = 0

# while principle <=0:
while True:
    principle=float(input("Enter the principle amount:"))
    if principle<0:
        print("Principle can't be less than or equal to zero")
    # print(principle)
    else:
        break

# while rate <=0:
while True:
    rate=float(input("Enter the Intrest rate:"))
    if rate<0:
        print("rate can't be less than or equal to zero")
    # print(rate)
    else:
        break

# while time <=0:
    time=int(input("Enter the time in years:"))
    if time<0:
        print("Time can't be less than or equal to zero")
    # print(time)
    else:
        break

total = principle*pow((1+rate/100),time)
print(f"Balance after {time} years /s: ${total:.2f}")