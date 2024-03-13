import argparse
import re


def generate_layer_string(num_layers):
    layer_template = """
    [
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

      {0}row1pos01,
      {0}row1pos02,
      {0}row1pos03,
      {0}row1pos04,
      {0}row1pos05,
      {0}row1pos06,
      "KC_NO",

      "KC_NO",
      {0}row1pos07,
      {0}row1pos08,
      {0}row1pos09,
      {0}row1pos10,
      {0}row1pos11,
      {0}row1pos12,

      {0}row2pos01,
      {0}row2pos02,
      {0}row2pos03,
      {0}row2pos04,
      {0}row2pos05,
      {0}row2pos06,

      {0}row2pos07,
      {0}row2pos08,
      {0}row2pos09,
      {0}row2pos10,
      {0}row2pos11,
      {0}row2pos12,

      {0}row3pos01,
      {0}row3pos02,
      {0}row3pos03,
      {0}row3pos04,
      {0}row3pos05,
      {0}row3pos06,
      "KC_NO",

      "KC_NO",
      {0}row3pos07,
      {0}row3pos08,
      {0}row3pos09,
      {0}row3pos10,
      {0}row3pos11,
      {0}row3pos12,

      "KC_NO",
      "KC_NO",
      "KC_NO",
      "KC_NO",
      {0}row4pos01,
      {0}row4pos06,
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
      {0}row4pos02,
      {0}row4pos03,
      "KC_NO",
      "KC_NO",
      {0}row4pos05,
      {0}row4pos06
    ]
    """
    layers = []
    for i in range(1, num_layers + 1):
        layer = layer_template.format(f"layer{i}")
        layers.append(layer.strip())
    return ",\n".join(layers)


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
                layers_string = generate_layer_string(num_layers)

                config_template = f"""{{
  "version": 1,
  "notes": "",
  "documentation": "",
  "keyboard": "ergodox_ez/base",
  "keymap": "hellmak-ergodox",
  "layout": "LAYOUT_ergodox_pretty",
  "layers": [
    {layers_string}
  ],
  "author": ""
}}"""

                with open(args.output, 'w') as output_file:
                    output_file.write(config_template)
                print(f"Configuration written to {args.output}")
            else:
                print("No 'layer[number]' pattern found in the last line.")

    except FileNotFoundError:
        print(f"File not found: {args.file}")


if __name__ == "__main__":
    main()

