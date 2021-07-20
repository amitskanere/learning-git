            #examole of functions
def new_user(first_name, last_name):
    print(f'hello {first_name} {last_name}')
    print("bye bye")


print("start")
new_user("john", "smith")
print("end")

#keyword argument , it improves readability of code it shuold alwys come after positional argument
def old_user(first_name,last_name):
    print(f"hello {first_name} {last_name}")

print("\nstart")
old_user(last_name="kanere",first_name="amit")
print("end")



def square(number):
    return number*number

print("\n",square(8))
