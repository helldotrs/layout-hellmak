import json


def map_keys(unicorne_key):
    # Placeholder function for key mapping
    # Add your specific key mapping logic here
    # For simplicity, this returns the key itself
    return unicorne_key


def convert_layout(unicorne_json_path):
    try:
        with open(unicorne_json_path, 'r') as file:
            unicorne_layout = json.load(file)
    except Exception as e:
        print(f"Failed to read {unicorne_json_path}: {e}")
        return

    ergodox_layout = {
        "version": 1,
        "notes": "",
        "documentation": unicorne_layout["documentation"],
        "keyboard": "ergodox_ez",
        "keymap": unicorne_layout["keymap"] + "_ergodox",
        "layout": "LAYOUT_ergodox",
        "layers": [],
        "author": unicorne_layout["author"]
    }

    for layer in unicorne_layout["layers"]:
        ergodox_layer = []
        # Mapping the base row and adding placeholders for extra ErgoDox keys
        ergodox_layer.append(layer[:6] + ["KC_NO"] * 2 + layer[6:12])  # Top row, adding placeholders for F-keys later

        # Assume layers are of equal length and map directly
        for row in range(1, 3):  # Mapping direct keys
            ergodox_layer.append(layer[row * 12:(row + 1) * 12])

        # Add placeholders for the ErgoDox thumb cluster
        ergodox_layer.append(["KC_NO"] * 12)  # Placeholder for the thumb cluster keys

        # Adjusting keys and mapping function, assuming a simplistic direct mapping
        mapped_layer = [[map_keys(key) for key in row] for row in ergodox_layer]

        # Append the modified layer to the ErgoDox layout
        ergodox_layout["layers"].append(mapped_layer)

    # Save the new ErgoDox layout to a JSON file
    output_filename = unicorne_json_path.replace(".json", "_ergodox.json")
    try:
        with open(output_filename, 'w') as file:
            json.dump(ergodox_layout, file, indent=4)
        print(f"ErgoDox layout has been saved to {output_filename}")
    except Exception as e:
        print(f"Failed to write {output_filename}: {e}")


def main():
    filename = input("Enter the filename of the Unicorn V3 layout JSON: ")
    convert_layout(filename)


if __name__ == "__main__":
    main()
