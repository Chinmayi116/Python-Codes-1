for i in range(1, 11):
    basic = float(input(f"Enter Basic Salary of Employee {i}: "))

    if basic < 10000:
        da = 0.50 * basic
        hra = 0.05 * basic
    elif basic <= 30000:
        da = 0.70 * basic
        hra = 0.10 * basic
    else:
        da = 1.00 * basic
        hra = 0.20 * basic

    gross = basic + da + hra

    print(f"Employee {i} Gross Salary = {gross}\n")
