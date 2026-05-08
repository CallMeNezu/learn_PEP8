def validate_age(age):
    if age <= 0 or age >= 150:
        if age < 18:
            return "minor"
        elif age >= 18 and age < 65:
            return "adult"
        else:
            return "senior"
    else:
        return "invalid"

x = 10
y = 20
z = 30
if x < y and y < z:
    print("Increasing sequence")