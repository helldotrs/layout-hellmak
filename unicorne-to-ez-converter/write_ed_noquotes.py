import argparse
import re
import json


def generate_layers(num_layers):
    layers = []
    for i in range(1, num_layers + 1):  # Start from 1 to num_layers inclusive
        layer = [
            "KC_F12",
            "KC_F11",
            "KC_F10",
            "KC_F9",
            "KC_F8",
            "KC_F7",
            "KC_NO",

            "KC_NO",
            "KC_F1",
            "KC_F2",
            "KC_F3",
            "KC_F4",
            "KC_F5",
            "KC_F6",

            f"layer{i}row1pos01",
            f"layer{i}row1pos02",
            f"layer{i}row1pos03",
            f"layer{i}row1pos04",
            f"layer{i}row1pos05",
            f"layer{i}row1pos06",
            "KC_NO",

            "KC_NO",
            f"layer{i}row1pos07",
            f"layer{i}row1pos08",
            f"layer{i}row1pos09",
            f"layer{i}row1pos10",
            f"layer{i}row1pos11",
            f"layer{i}row1pos12",

            f"layer{i}row2pos01",
            f"layer{i}row2pos02",
            f"layer{i}row2pos03",
            f"layer{i}row2pos04",
            f"layer{i}row2pos05",
            f"layer{i}row2pos06",

            f"layer{i}row2pos07",
            f"layer{i}row2pos08",
            f"layer{i}row2pos09",
            f"layer{i}row2pos10",
            f"layer{i}row2pos11",
            f"layer{i}row2pos12",

            f"layer{i}row3pos01",
            f"layer{i}row3pos02",
            f"layer{i}row3pos03",
            f"layer{i}row3pos04",
            f"layer{i}row3pos05",
            f"layer{i}row3pos06",
            "KC_NO",

            "KC_NO",
            f"layer{i}row3pos07",
            f"layer{i}row3pos08",
            f"layer{i}row3pos09",
            f"layer{i}row3pos10",
            f"layer{i}row3pos11",
            f"layer{i}row3pos12",

            "KC_NO",
            "KC_NO",
            "KC_NO",
            "KC_NO",
            f"layer{i}row4pos01",
            f"layer{i}row4pos06",
            "KC_NO",
            "KC_NO",
            "KC_NO",
            "KC_NO",
            "KC_NO",
            "KC_NO",
            "KC_NO",
            "KC_NO",
            "KC_NO",
            "KC_NO",
            f"layer{i}row4pos02",
            f"layer{i}row4pos03",
            "KC_NO",
            "KC_NO",
            f"layer{i}row4pos05",
            f"layer{i}row4pos06"
        ]
        layers.append(layer)
    return layers


def main():
    parser = argparse.ArgumentParser(description="Generate keyboard layers from a template.")
    parser.add_argument("--file", help="The path to the file to be processed.")
    parser.add_argument("--output", help="The path to the output file.")
    args = parser.parse_args()

    if args.file is None:
        print("Please specify a file path using --file")
        return

    if args.output is None:
        print("Please specify an output file path using --output")
        return

    try:
        with open(args.file, 'r') as file:
            lines = file.readlines()
            last_line = lines[-1] if lines else ""

            match = re.search(r'layer(\d+)', last_line)
            if match:
                num_layers = int(match.group(1))
                layers = generate_layers(num_layers)

                # Prefix
                keyboard_config = {
                    "version": 1,
                    "notes": "",
                    "documentation": "",
                    "keyboard": "ergodox_ez/base",
                    "keymap": "hellmak-ergodox",
                    "layout": "LAYOUT_ergodox_pretty",
                    "layers": layers,
                    "author": ""
                }

                # Write the keyboard configuration to the output file
                with open(args.output, 'w') as output_file:
                    json.dump(keyboard_config, output_file, indent=2)

                print(f"Configuration has been written to {args.output}")
            else:
                print("No 'layer[number]' pattern found in the last line.")

    except FileNotFoundError:
        print(f"File not found: {args.file}")


if __name__ == "__main__":
    main()
