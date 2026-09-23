def add_Subject():
    subject = input("Enter subject name: ")
    print("subject added ", subject)
    


print ("==============================")
print ("   AI Study Assistant📚🤖")
print ("==============================")

print("1.Add subject", "2.Note", "3.Search note", "4.Quiz", "5.Progress" , "6.Exit")

choice = int(input("Enter your choice: "))

print("Your choice is", choice)

if choice == 1:
    add_Subject()