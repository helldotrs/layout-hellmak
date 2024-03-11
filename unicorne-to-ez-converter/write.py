import argparse
import re

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Process an input file.")
    parser.add_argument("--file", help="The path to the file to be processed.")
    args = parser.parse_args()

    # Ensure a file path was provided
    if args.file is None:
        print("Please specify a file path using --file")
        return

    # Try to open and read the file
    try:
        with open(args.file, 'r') as file:
            lines = file.readlines()
            last_line = lines[-1] if lines else ""

            # Use regular expression to find the number after "layer" in the last line
            match = re.search(r'layer(\d+)', last_line)
            if match:
                layer_number = match.group(1)
                print(f"The number after 'layer' in the last line is: {layer_number}")
            else:
                print("No 'layer[number]' pattern found in the last line.")

    except FileNotFoundError:
        print(f"File not found: {args.file}")

if __name__ == "__main__":
    main()
