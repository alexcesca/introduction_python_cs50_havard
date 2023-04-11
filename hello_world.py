#ask user for their name
name = input("What's your first name? ")

#remove whitespacre from str
#name = name.strip();

#Capitalise user's name
#Capitalize upper only first cchar.
#name = name.capitalize();

# Title upper all first char
#name = name.title()

# remove whitespace end upper fisrt char in one line
name = name.strip().title()

#another possibilit is add on input
last_name = input("What's your last name? ").strip().title()

#say hello to user
print(f"hello,  {name} {last_name}")