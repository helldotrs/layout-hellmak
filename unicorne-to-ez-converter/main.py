import json

def convert_unicorne_to_ergodox(unicorne_layout):
    ergodox_layers = []

    for layer in unicorne_layout["layers"]:
        ergodox_layer = []
        # Initialize ErgoDox layer with placeholders
        for _ in range(14):  # ErgoDox has more keys per row in some cases
            ergodox_layer.append(["KC_NO"] * 7 + ["KC_TRNS"] * 2 + ["KC_NO"] * 5)  # Adjust according to ErgoDox's layout

        # Map Unicorn V3 keys to ErgoDox layout positions
        for i, key in enumerate(layer):
            row, col = divmod(i, 12)  # Assuming 12 keys per row in Unicorn V3 layout for simplicity

            # Directly map keys to the corresponding ErgoDox positions
            # This is a simplification; actual mapping may require adjustments
            if row < 3:  # For main key rows
                if col < 6:  # Left side of the split
                    ergodox_layer[row][col] = key
                elif col > 5:  # Right side of the split
                    ergodox_layer[row][col+2] = key  # Adjust for the middle gap in ErgoDox layout
            elif row == 3:  # For bottom row, map to thumb cluster if needed
                # Simplified: you might want to map these keys to thumb clusters or other areas in ErgoDox
                if col < 6:  # Left thumb cluster area (simplified mapping)
                    ergodox_layer[3][col] = key
                elif col > 5:  # Right thumb cluster area (simplified mapping)
                    ergodox_layer[3][col+2] = key

        ergodox_layers.append(ergodox_layer)

    return ergodox_layers

def main():
    filename = input("Enter the filename of the Unicorn V3 layout JSON: ")
    output_filename = filename.replace(".json", "_ergodox.json")

    try:
        with open(filename, 'r') as file:
            unicorne_layout = json.load(file)

        ergodox_layers = convert_unicorne_to_ergodox(unicorne_layout)

        # Prepare the ErgoDox JSON structure
        ergodox_json = unicorne_layout  # Start with the Unicorn V3 layout as a base for simplicity
        ergodox_json["keyboard"] = "ergodox_ez"  # Change to ErgoDox
        ergodox_json["keymap"] += "_ergodox"  # Append to keymap name
        ergodox_json["layout"] = "LAYOUT_ergodox_pretty"  # Adjust layout name if necessary
        ergodox_json["layers"] = ergodox_layers  # Replace layers with converted layers

        with open(output_filename, 'w') as file:
            json.dump(ergodox_json, file, indent=4)

        print(f"ErgoDox layout has been saved to {output_filename}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
