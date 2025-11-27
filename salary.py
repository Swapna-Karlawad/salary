import sys

if len(sys.argv) != 2:
    print("Usage: python salary_bonus.py <salary>")
    sys.exit(1)

script_name = sys.argv[0]

try:
    salary = float(sys.argv[1])
except:
    salary = 10000     # default salary

bonus = salary * 0.10
total = salary + bonus

print("script Name:", script_name)
print("Bonus:", bonus)
print("Total Salary:", total)
