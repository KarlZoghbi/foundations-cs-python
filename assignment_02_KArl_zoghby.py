def displayMenu():
  print("1. Count digist\n" + "2. Find Max\n" + "3. Count Tags\n" + "4. Exit\n" + "- - - - - - - - - - - - - - -" )

def countDigit(number):
    if number > 10:
        return 1
    return 1 + countDigit(number // 10)
  
  

    
def findMax(lst):
    if not lst:  
        return 0

    if len(lst) == 1: 
        return lst[0]

   
    rest_max = find_max_recursive(lst[1:])
    return lst[0] if lst[0] > rest_max else rest_max
    

def count_tag_occurrences(html, tag):
    opening_tag = "<{}>".format(tag)
    closing_tag = "</{}>".format(tag)
    start_index = html.find(opening_tag)
    
    if start_index == -1:
        return 0

    end_index = html.find(closing_tag, start_index)
    
    if end_index == -1:
        return 0

    remaining_html = html[end_index + len(closing_tag):]
    
    return 1 + count_tag_occurrences(remaining_html, tag)
  




def main():
  displayMenu()  # this function simply prints the menu
  choice = int(input("please enter your choice here: "))

  while (choice != 4):
    if (choice == 1):
      num = int(input("please enter a number: "))
      print(countDigit(num))
      
    elif (choice == 2):
      input_list = input("Enter a list of integers (space-separated): ").split()
      input_list = [int(num) for num in input_list]
      max_value = findMax(input_list)
      print("Maximum value:", max_value)
    elif (choice == 3):
      html_code = input("Enter the HTML code: ")
      tag = input("Enter the tag to count: ")
      occurrences = count_tag_occurrences(html_code, tag)
      print("Occurrences of <{}>: {}".format(tag, occurrences))
    else:
      print("this is an invalid choice ")

    displayMenu()
    choice = int(input("please enter your choice here: "))

  print("Thank you for using my program!, you exited")


main()
  
  