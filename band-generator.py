#Go to: https://replit.com/@appbrewery/band-name-generator-start?v=1

#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5. Make sure the input cursor shows on a new line:

# Solution: https://replit.com/@appbrewery/band-name-generator-end

# This is a greetings -------->
print("Hello! Welcome to the Band Name Generator!")

# The user can choose Y or N of they would like to create a Band Name
answer = input("Would you like to create one?\nType [Y] if yes, Type [N] if no: ")
if answer == 'Y':
  city = input("What city you grew up? ")
elif answer == 'N':
  print("It's okay! Let's try later.")
# After they answer N the program will now exit
  exit()
  
pet = input("Cool! And give us a name of a pet / your pet:\n")
# After giving the user inputs, this will be combined here and can make a Band Name
print("Hey! Check this out!\nThis would be your Band Name!\n" + ":" +city +" "+ pet)
# End of the code