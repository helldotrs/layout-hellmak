import argparse
import re

def process_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as file:
        for line in lines:
            # This regular expression now specifically looks for "layer" followed by anything and ending with a comma
            if re.search(r'layer\S*,', line):
                file.write('      "KC_NO",\n')
            else:
                file.write(line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process input file to replace specific lines and output to a new file.')
    parser.add_argument('--input', '-i', type=str, required=True, help='Input file path')
    parser.add_argument('--output', '-o', type=str, required=True, help='Output file path')

    args = parser.parse_args()
    process_file(args.input, args.output)
