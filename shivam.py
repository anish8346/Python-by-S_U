class BMICalculator:
    def __init__(self, height_feet, weight_kg):
        self.height_feet = height_feet
        self.weight_kg = weight_kg

    def calculate_bmi(self):
        # Convert height from feet to meters
        height_meters = self.height_feet * 0.3048

        # Calculate BMI
        bmi = self.weight_kg / (height_meters ** 2)
        return bmi

    def get_bmi_category(self, bmi):
        # Determine BMI category
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"

def main():
    print("Welcome to the BMI Calculator!")

    try:
        # Input height in feet and weight in kilograms
        height_feet = float(input("Enter your height in feet: "))
        weight_kg = float(input("Enter your weight in kilograms: "))

        if height_feet <= 0 or weight_kg <= 0:
            print("Height and weight must be positive values. Please try again.")
            return

        # Create an instance of BMICalculator
        bmi_calculator = BMICalculator(height_feet, weight_kg)

        # Calculate BMI
        bmi = bmi_calculator.calculate_bmi()

        # Get BMI category
        category = bmi_calculator.get_bmi_category(bmi)

        # Display results
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}")

    except ValueError:
        print("Invalid input. Please enter numerical values for height and weight.")

# Run the program
if __name__ == "__main__":
    main()
