#Tax Calculator: Write a program to calculate the income tax for a given annual 
#income. The tax rates are:
#Income <= 20,000: Rs 200
#20,001 <= Income <= 50,000: 20% tax
#50,001 <= Income <= 70,000: 30% tax
#70,001 <= income <= 100,000 : 36% tax
#Income > 100,000: 42% tax
income = int(input())
if income<=20000:
    print("Rs 200")
elif (income>=20001 and income<=50000):
    print(f'tax :Rs.{income*0.2}')
elif (income>=50001 and income<=70000):
    print(f'tax :Rs.{income*0.3}')
elif (income>=70001 and income<=100000):
    print(f'tax :Rs.{income*0.36}')
elif (income>100000):
    print(f'tax :Rs.{income*0.42}')
