import json
import argparse

def load_and_assign_variables_from_unicorne(unicorne_file_path):
    # Load the Unicorne layout
    with open(unicorne_file_path, 'r') as file:
        unicorne_layout = json.load(file)

    # Dynamically handling multiple layers
    for layer_index, layer in enumerate(unicorne_layout['layers'], start=1):
        for key_index, key in enumerate(layer, start=1):
            row = (key_index-1) // 6 + 1  # Determine row based on index
            pos = (key_index-1) % 6 + 1   # Determine position in row
            variable_name = f'layer{layer_index}row{row}pos{pos:02}'
            globals()[variable_name] = key

            # Print variables in the format "variable_name: "value""
            print(f'{variable_name}: "{globals()[variable_name]}"')

def main():
    parser = argparse.ArgumentParser(description='Convert Unicorne layout JSON to variables.')
    parser.add_argument('--file', type=str, help='Path to the Unicorne layout JSON file', required=True)
    
    args = parser.parse_args()
    load_and_assign_variables_from_unicorne(args.file)

if __name__ == '__main__':
    main()
