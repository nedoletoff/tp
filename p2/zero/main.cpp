#include <iostream>
#include <string>
extern char _cipher(char, char);
extern char _next_key(char);

int main() {
    char seed;
    std::string str;
    std::string crypt_str;
    register unsigned char r;

    std::cout << "Enter string: ";

flag: getline(std::cin, str, '\n');
      if (str.length() == 0) {
          std::cout << "Error" << std::endl;
          goto flag;
      }

    crypt_str = str;

flag1: std::cout << "Enter key: ";
    std::cin >> r;
    if (r == 0) {
        std::cout << "Error" << std::endl;
        goto flag1;
    }

    std::cin.clear();

    std::cin.ignore();
    std::cout << "key " << r << std::endl;
    seed = r;

    std::cout << "Encrypted text: ";
    for (int i = 0; i < str.length(); i++) {
        crypt_str[i] = _cipher(str[i], seed);
        seed = _next_key(seed);
    }
    std::cout << crypt_str << std::endl;

flag2: std::cout << "Enter key: ";
    std::cin >> r;
    if (r == 0) {
        std::cout << "Error" << std::endl;
        goto flag2;
    }

    std::cin.clear();
    std::cin.ignore();
    std::cout << "key " << r << std::endl;
    seed = r;

    std::cout << "Decrypted text: ";
    for (int i = 0; i < str.length(); i++) {
        str[i] = _cipher(crypt_str[i], seed);
        seed = _next_key(seed);
    }
    std::cout << str << std::endl;

    return 0;
}

