def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


weight = 70
height = 1.75

bmi = calculate_bmi(weight, height)

print("BMI Calculator")
print(f"Weight: {weight} kg")
print(f"Height: {height} m")
print(f"BMI: {bmi:.2f}")