#This is a program that does a sequential search of an ordered set and stops when your target is less than the position in the list.
#Exercise 3.1
#By James Eaton
#Big-O for best case is O(1)
#Big-O for average is O(n)
#Big-O for worst is O(n)


def seqSearch(target, lyst):
    position = 0                                #Starts the search at position 1 in the list.

    while position < len(lyst):                 #Searches the entire list.
        if target == lyst[position]:
            return str(target) + " is in the list at position " + str(position)
                                                #If the target is a this position in lyst, it prints the position in which the target is located.
        
        elif target < lyst[position]:
            return str(target) + " is NOT in the list. The program stopped looking for your number at position " + str(position) + " because your list is in order."
                                                #If the target is not in the ordered list before target < the position, then the search halts.
        
        position += 1                           #Keeps incrimenting the position by 1 for each pass of the loop.



def main():
    lyst = []                                   #Starts the lyst empty.
    n = input("Enter an element to put into the list. <Enter nothing to quit>: ")
                                                #User enters an element to be put into the lyst.
    while n != "":                              #Keeps adding the elements entered by the user until the user presses enter with nothing to be added.
        lyst.append(n)
        n = input("Enter an element to put into the list <Enter nothing to quit>: ")

    target = input("Enter an element you want to search for: ")

    
    print("You entered" , lyst)                 #Shows your unsorted lyst
    print()
    lyst.sort()                                 #Sorts the lyst.
    print("After sorting, your list looks like" , lyst)
                                                #Shows your sorted lyst.
    print()
    print(seqSearch(target, lyst))

main()
