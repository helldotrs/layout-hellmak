import argparse
import re

def parse_arguments():
    parser = argparse.ArgumentParser(description="Replace variable names with values in a text file.")
    parser.add_argument("-l", "--layout", required=True, help="Path to the layout text file.")
    parser.add_argument("-v", "--values", required=True, help="Path to the Python file containing variable values.")
    parser.add_argument("-o", "--output", required=True, help="Path to the output text file.")
    return parser.parse_args()

def read_variables(file_path):
    variables = {}
    with open(file_path, 'r') as file:
        for line in file:
            # Assuming each line is in the format: var_name = "value"
            match = re.match(r'(\w+)\s*=\s*"(.*)"', line)
            if match:
                variables[match.group(1)] = match.group(2)
    return variables

def replace_variables_in_layout(layout_path, variables, output_path):
    with open(layout_path, 'r') as file:
        layout_content = file.read()

    for var_name, var_value in variables.items():
        # Replace variable name with its value (including quotation marks)
        layout_content = layout_content.replace(var_name, f'"{var_value}"')

    with open(output_path, 'w') as file:
        file.write(layout_content)

def main():
    args = parse_arguments()
    variables = read_variables(args.values)
    replace_variables_in_layout(args.layout, variables, args.output)

if __name__ == "__main__":
    main()
