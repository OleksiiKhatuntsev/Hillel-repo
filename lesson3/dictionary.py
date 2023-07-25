employees_dict = {"testmail@gmail.com": "Test Employee 1",
                  "testmail1@gmail.com": 2,
                  1: "testemployee" }


print(employees_dict)
print(employees_dict["testmail@gmail.com"])
print(employees_dict[1])
employees_dict[2] = 5
employees_dict[1] = "NEW VALUE"
print(employees_dict[2])
print(employees_dict[1])
print(len(employees_dict))

# dict = changeable , ordered\unordered
