is_male = True
is_tall = True

if is_male and is_tall:
    print("Tall male")
elif is_male and not is_tall:
    print("Short male")
elif not is_male and is_tall:
    print("Not male but tall")
else:
    print("You are not male or tall")