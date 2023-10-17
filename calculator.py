num1 = 0;
num2 = 0;
operation = "";
result = "";

def calculation(num1, num2):
	num1 = int(num1);
	num2 = int(num2);
	if operation == "+":
		result = num1 + num2;
	elif operation == "-":
		result = num1 - num2;
	elif operation == "*":
		result = num1 * num2;
	elif operation == "/":
		result = num1 / num2;
	elif operation == "%":
		result = num1 % num2;
	else:
		print("Unsupported operation");
	return result;

num1 = input("Enter your first number: ");
operation = input("Enter an operation +, -, *, /, or %: ");
num2 = input("Enter your second number: ");
result = calculation(num1, num2);

print("Your result is", result);