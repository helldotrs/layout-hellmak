"""
Usage:
$ python3 main.py --file <path_to_unicorne_layout.json> --output <path_to_output_python_file.py>
Example:
$ python3 main.py --file unicorne/uc_hellmak_23_atmosphere.json --output temp/variables.py
"""

import json
import argparse

def load_and_assign_variables_from_unicorne(unicorne_file_path, output_file_path):
    # Load the Unicorne layout
    with open(unicorne_file_path, 'r') as file:
        unicorne_layout = json.load(file)

    with open(output_file_path, 'w') as output_file:
        # Write a header to the output file
        output_file.write("# Generated variables from Unicorne layout\n\n")
        
        # Dynamically handling multiple layers
        for layer_index, layer in enumerate(unicorne_layout['layers'], start=1):
            for key_index, key in enumerate(layer, start=1):
                row = (key_index-1) // 6 + 1  # Determine row based on index
                pos = (key_index-1) % 6 + 1   # Determine position in row
                variable_name = f'layer{layer_index}row{row}pos{pos:02}'
                
                # Write variables in the format "variable_name = 'value'" to the output file
                output_file.write(f'{variable_name} = "{key}"\n')

def main():
    parser = argparse.ArgumentParser(description='Convert Unicorne layout JSON to Python variables.')
    parser.add_argument('--file', type=str, help='Path to the Unicorne layout JSON file', required=True)
    parser.add_argument('--output', type=str, help='Output Python file for the variables', required=True)
    
    args = parser.parse_args()
    load_and_assign_variables_from_unicorne(args.file, args.output)

if __name__ == '__main__':
    main()
