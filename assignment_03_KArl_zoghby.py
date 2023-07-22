import json


def displayMenu():
  print("1. Sum Tuples\n" + "2. Export JSON\n" + "3. Import JSON\n" +
        "4. Exit\n" + "- - - - - - - - - - - - - - -")


def sumTuples(tup1, tup2):
  if len(tup1) != len(tup2):
    return ("Input tuples must be of the same length")

  result = ()
  for i in range(len(tup1)):
    sum_value = int(tup1[i]) + int(tup2[i])
    result += (sum_value, )

  return result
  
def writeJson(data_dict, filename):
    json_str = "{\n"
    for i, j in data_dict.items():
        json_str += f'    "{i}": {json.dumps(j)},\n'
    json_str = json_str.rstrip(",\n")
    json_str += "\n}"

    with open(filename, "w") as file:
        file.write(json_str)

def readJson(filename):
    objects_list = []

    with open(filename, "r") as file:
        json_data = json.load(file)

    if isinstance(json_data, list):
        objects_list = json_data
    elif isinstance(json_data, dict):
        objects_list.append(json_data)

    return objects_list

def main():
  displayMenu()  # this function simply prints the menu
  choice = int(input("please enter your choice here: "))

  while (choice != 4):
    if (choice == 1):
      tuple1 = tuple(
        input("enter a list of numbers seperated by spaces: ").split())
      tuple2 = tuple(
        input("enter a list of numbers seperated by spaces: ").split())
      result = sumTuples(tuple1, tuple2)
      print(result)

    elif (choice == 2):
        data = {
        "name": "Karl Zoghbe",
        "age": 19,
        "is_employed": True,
        "hobbies": ["coding", "hiking", "swimming"],
        "address": {
        "city": "Beirut"
        }
    }
        file_name = "data.json"
        writeJson(data, file_name)
    elif (choice == 3):
        file_name = "data.json"
        result_list = readJson(file_name)
        print(result_list)
    else:
      print("this is an invalid choice ")

    displayMenu()
    choice = int(input("please enter your choice here: "))

  print("Thank you for using my program!, you exited")


main()

# a. O(N^3)
# b. O(N^3)
# c. O(N!)
# d. O(NlogN)
# e. O(N)
# f. O(N^2)
# g. O(N^2)
# h. O(N!)