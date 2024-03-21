from rpn_calculator import RPNCalculator
from pathlib import Path

def main():
    input_file = input("Enter the file path")
    output_file = input("Enter the file path")
    input_file = Path(input_file)
    output_file = Path(output_file)

    try:
        with open(input_file, 'r') as f:
            expressions = f.read().splitlines()

        calculator = RPNCalculator()
        results = []

        for expression in expressions:
            result = calculator.evaluate_rpn(expression)
            results.append(str(result))

        with open(output_file, 'w') as f:
            f.write('\n'.join(results))

        print("Results written to", output_file)

    except FileNotFoundError:
        print("File not found:", input_file)

if __name__ == "__main__":
    main()