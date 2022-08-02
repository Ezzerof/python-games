# Creating a empty list to store our variables.
names = []
ages = []
gender = []
salaries = []
sum_fem_ages=0
sum_male_ages=0
sum_fem_sal=0
sum_male_sal=0

n = int(input("Enter number of employees: "))
for i in range(0,n):
    name= input("Enter employee Name: ")
    names.append(name)
    age = int(input("Enter employee Age: "))
    ages.append(age)
    genders= input("Enter employee Gender: ")
    gender.append(genders)
    salary = float(input("Enter employee Salary: "))
    salaries.append(salary)

# Finding indexes of F and M, after that counting ages and salaries from the list by their indexes

for i in range(len(gender)):
    if gender[i]=="F":
        sum_fem_ages+=ages[i]
        sum_fem_sal+=salaries[i]
    elif gender[i]=="M":
        sum_male_ages+=ages[i]
        sum_male_sal+=salaries[i]

print("Names: ", " ", names)
print("Ages are: ", " ", ages)
print("Genders are: ", " ", gender)
print("Salaries are: ", " ", salaries)

print("\nThe average of men ages is: "+ str(sum_male_ages/gender.count("M")) +" years.\n" +
      "The average of women ages is: " + str(sum_fem_ages/gender.count("F")) + " years.\n" +
      "The average of men salaries is: " + "£" + str(round(sum_male_sal/gender.count("M"),2)) +
      "\nThe average of women salaries is: " + "£" + str(round(sum_fem_sal/gender.count("F"),2)))