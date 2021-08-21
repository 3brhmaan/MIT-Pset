annual_salary = float(input("Enter your annual salary : "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal : "))
salary_saved_evry_month = (annual_salary / 12)*portion_saved
total_cost = float(input("Enter the cost of your dream home : "))
portion_down_payment = .25 * total_cost
mont_rate = .04 / 12
saved = 0.0
saved = salary_saved_evry_month + saved*mont_rate
month = 1
while saved < portion_down_payment :
    saved += salary_saved_evry_month  + saved*mont_rate
    month+=1
print("Number of months :",month)
