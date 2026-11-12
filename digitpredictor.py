
# Training data
digits = [1, 2, 3, 2, 5, 2, 7, 2, 8, 9]

# Find the most frequent digit
def train(data):
    frequency = {}

    for digit in data:
        if digit in frequency:
            frequency[digit] += 1
        else:
            frequency[digit] = 1

    return max(frequency, key=frequency.get)


# Train the predictor
prediction = train(digits)

print("Training Data:", digits)
print("Predicted Digit:", prediction)

# Test with user input
number = int(input("Enter a digit: "))

if number == prediction:
    print("Prediction is correct!")
else:
    print("Prediction was:", prediction)
