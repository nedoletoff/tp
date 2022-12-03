#include "func.h"

char next_key(char prev_key) {
  char res;
  asm(".intel_syntax noprefix\n\t"
      "mov eax, %1;\n\t"
      "rcr eax, 1\n\t"
      "mov %0, al;\n\t"
      :"=r"(res)
      :"r"(prev_key)
      :"eax"
     );
  return res;
}

char cipher(char symbol, char gamma) {
  char res;
  asm(".intel_syntax noprefix\n\t"
      "mov eax, %1;\n\t"
      "mov ebx, %2;\n\t"
      "xor eax, ebx;\n\t"
      "mov %0, eax;\n\t"
      :"=r"(res)
      :"r"(symbol), "r"(gamma)
      :"eax"
     );
    return symbol;
}

