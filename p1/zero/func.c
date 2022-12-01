#include "func.h"


unsigned char key;

int get_key() {
    return key;
}

void next_key() {
    unsigned char k = 1;
    key = (key >> k) | (key << (sizeof(key) * 8 - k));
}

void seed(unsigned char new_key) {
    key = new_key;
}

char cipher(char symbol, char gamma) {
    return symbol ^ gamma;
}




