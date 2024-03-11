import json

def convert_unicorne_to_ergodox(unicorne_layout):
    # Initialize ErgoDox layer with KC_NO for all positions
    ergodox_layer = ["KC_NO"] * 76  # ErgoDox has 76 keys in its layout

    # Direct mapping of keys from Unicorne to ErgoDox, considering typical layout positions
    # This is a simplification. You'll need to adjust indices based on your mapping requirements
    unicorne_to_ergodox_index_map = [
        # Left hand side
        15, 16, 17, 18, 19, 20,  # Row 1 (top row, excluding function keys and the first key)
        29, 30, 31, 32, 33, 34,  # Row 2
        44, 45, 46, 47, 48, 49,  # Row 3
        57, 58, 59, 60, 61,      # Row 4 (shift and below)
        # Right hand side
        24, 25, 26, 27, 28,  # Row 1 (top row, starting right from the middle keys)
        38, 39, 40, 41, 42, 43,  # Row 2
        52, 53, 54, 55, 56,  # Row 3
        62, 63, 64, 65, 66   # Row 4 (shift and below)
    ]

    # Fill the ErgoDox layer based on the Unicorne layer mapping, skipping "KC_NO" and function keys
    for u_index, key in enumerate(unicorne_layout['layers'][0]):
        if key not in ["KC_NO", "KC_TRNS"] and not key.startswith("KC_F"):
            # Map the key from Unicorne to the corresponding ErgoDox position
            e_index = unicorne_to_ergodox_index_map[u_index]
            ergodox_layer[e_index] = key

    # Add function keys manually for the ErgoDox layout, assuming F1-F12 are to be placed on the leftmost top row
    for i, f_key in enumerate(["KC_F1", "KC_F2", "KC_F3", "KC_F4", "KC_F5", "KC_F6", "KC_TRNS", "KC_TRNS", "KC_F7", "KC_F8", "KC_F9", "KC_F10", "KC_F11", "KC_F12"]):
        ergodox_layer[i] = f_key

    return [ergodox_layer]

def main():
    unicorne_filename = input("Enter the full path of the Unicorne layout JSON file: ")
    unicorne_layout = json.load(open(unicorne_filename, 'r'))
    
    ergodox_converted_layers = convert_unicorne_to_ergodox(unicorne_layout)

    # Prepare the output filename
    output_filename = unicorne_filename.replace(".json", "_ergodox.json")
    
    # Construct the ErgoDox layout JSON structure
    ergodox_layout = unicorne_layout  # Copy base structure from Unicorne
    ergodox_layout["keyboard"] = "ergodox_ez"
    ergodox_layout["keymap"] = unicorne_layout["keymap"] + "_ergodox"
    ergodox_layout["layout"] = "LAYOUT_ergodox"  # Ensure this matches the ErgoDox layout name in QMK
    ergodox_layout["layers"] = ergodox_converted_layers

    # Save the ErgoDox layout JSON
    with open(output_filename, 'w') as f:
        json.dump(ergodox_layout, f, indent=4)
    
    print(f"Converted ErgoDox layout saved to: {output_filename}")

if __name__ == "__main__":
    main()
