import argparse
import re


def load_values_from_py(values_file):
    values = {}
    with open(values_file, 'r') as file:
        exec(file.read(), values)
    return values


def replace_placeholders_with_values(layout_file, values):
    with open(layout_file, 'r') as file:
        layout_content = file.read()
    for key, value in values.items():
        layout_content = re.sub(f'(?<!")\\b{key}\\b(?!")', f'"{value}"', layout_content)
    return layout_content


def save_to_json(output_file, content):
    with open(output_file, 'w') as file:
        file.write(content)


def main():
    parser = argparse.ArgumentParser(
        description="Replace placeholders in layout file with values from variables file and output as JSON.")
    parser.add_argument('--layout', '-l', type=str, required=True, help='Layout file path.')
    parser.add_argument('--values', '-v', type=str, required=True, help='Values file path.')
    parser.add_argument('--output', '-o', type=str, required=True, help='Output JSON file path.')

    args = parser.parse_args()

    values = load_values_from_py(args.values)
    content = replace_placeholders_with_values(args.layout, values)
    save_to_json(args.output, content)


if __name__ == "__main__":
    main()
