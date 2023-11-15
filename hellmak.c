#include QMK_KEYBOARD_H

#define BASE_LAYER 0
#define FUNC_LAYER 1
#define NAV_LAYER  2
#define MEDIA_LAYER 3

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
  [BASE_LAYER] = LAYOUT(
    KC_Q,    KC_W,    KC_F,    KC_P,    KC_B,                   KC_J,    KC_L,    KC_U,    KC_Y,    KC_SCLN,
    KC_A,    KC_R,    KC_S,    KC_T,    KC_G,                   KC_M,    KC_N,    KC_E,    KC_I,    KC_O,
    KC_Z,    KC_X,    KC_C,    KC_D,    KC_V,                   KC_K,    KC_H,    KC_COMM, KC_DOT, KC_ENT,
    KC_ESC,  MO(FUNC_LAYER), KC_LCTL, KC_LALT,   KC_SPC,   MO(MEDIA_LAYER)
  ),

  [FUNC_LAYER] = LAYOUT(
    KC_1,    KC_2,    KC_3,    KC_4,    KC_5,                   KC_6,    KC_7,    KC_8,    KC_9,    KC_0,
    KC_TAB,  KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,                KC_TRNS, KC_LEFT, KC_DOWN, KC_UP,   KC_RGHT,
    KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,                KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,
    KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,   KC_TRNS,   KC_TRNS
  ),

  [NAV_LAYER] = LAYOUT(
    KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,                KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,
    KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,                KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,
    KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,                KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,
    KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,   KC_TRNS,   KC_TRNS
  ),

  [MEDIA_LAYER] = LAYOUT(
    KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,                KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,
    KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,                KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,
    KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,                KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,
    KC_TRNS, KC_TRNS, KC_TRNS, KC_TRNS,   KC_TRNS,   KC_TRNS
  )
};

void matrix_init_user(void) {
  // Call the matrix init function of each layer when the matrix initializes.
  matrix_init_user();
}

void matrix_scan_user(void) {
  // Call the matrix scan function of each layer when the matrix scans.
  matrix_scan_user();
}

bool process_record_user(uint16_t keycode, keyrecord_t *record) {
  switch (keycode) {
    // Add custom key processing here
  }
  return true;
}
