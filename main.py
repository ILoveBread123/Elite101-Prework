
try:
  user_name, user_age = input("What is your name and age? \n please enter in the following format: Dave 23 \n" ).split()
except ValueError:
  user_name = 'John Doe'
  user_age = 0

print(user_name)
print(int(user_age))

print(f'Welcome {user_name}!, I am (chatbot name)!')
user_request = input('What can I do for you?')

menu_loop = True

def menu():
  print("--Please choose from the menu below-- ")
  print("1. placeholder1")
  print("2. placeholder2")
  print("3. placeholder3")
  print("4. Exit")


def user_request():
  in_use = True
  user_choice = int(input("Enter your choice: "))
  if user_choice == 1:
    print("placeholder1")
  elif user_choice == 2:
    print("placeholder2")
  elif user_choice == 3:
    print('placeholder3')
  elif user_choice == 4:
    print("Goodbye!")
    in_use = False
  else:
    print("Invalid choice, please try again")
    return in_use


while menu_loop == True:
  menu()
  menu_loop = user_request()