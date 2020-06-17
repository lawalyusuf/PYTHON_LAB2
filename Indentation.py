#Indentation
#Indentation matters. Each line under the if statement that is indented will only be executed if the statement is true:


if a == 1:
    print("If a is one, this will print.")
    print("So will this.")
    print("And this.")
 
print("This will always print because it is not indented.")
#Indentation must be the same. This code doesn't work.

if a == 1:
  print("Indented two spaces.")
    print("Indented four. This will generate an error.")
   print("The computer will want you to make up your mind.")
#Once an if statement has been finished, it is not possible to re-indent to go back to it. The test has to be performed again.

if a == 1:
    print("If a is one, this will print.")
    print("So will this.")
 
print("This will always print because it is not indented.")
    print("This will generate an error. Why it is indented?")
