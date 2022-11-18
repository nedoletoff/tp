#include <string>
#include <iostream>

using namespace std;
unsigned char key1;
unsigned char key2;

void next_key() {
    register char temp = key2;
    key2 = key2 + key1;
    key1 = temp;
}

void seed(unsigned char new_key1, unsigned char new_key2 ) {
    key1 = new_key1;
    key2 = new_key2;
}

char cipher(char symbol, char gamma) {
    return symbol ^ gamma;
}

int main() {
    register string str;
    register string crypt_str;
    register unsigned int r1, r2;

    cout << "Enter string: ";

flag: getline(cin, str, '\n');
      if (str.length() == 0) {
          cout << "Error" << endl;
          goto flag;
      }

    crypt_str = str;

flag1: cout << "Enter key1: ";
    cin >> r1;
    if (r1 == 0) {
        cout << "Error" << endl;
        goto flag1;
    }

    cin.clear();
    cin.ignore();
    cout << "key1 " << r1 << endl;

flag2: cout << "Enter key2: ";
    cin >> r2;
    if (r2 == 0) {
        cout << "Error" << endl;
        goto flag3;
    }

    cin.clear();
    cin.ignore();
    cout << "key2 " << r2 << endl;


    seed(r1, r2);

    cout << "Encrypted text: ";
    for (int i = 0; i < str.length(); i++) {
        crypt_str[i] = cipher(str[i], key2);
        next_key();
    }
    cout << crypt_str << endl;


flag3: cout << "Enter key1: ";
    cin >> r1;
    if (r1 == 0) {
        cout << "Error" << endl;
        goto flag3;
    }

    cin.clear();
    cin.ignore();
    cout << "key1 " << r1 << endl;

flag4: cout << "Enter key2: ";
    cin >> r2;
    if (r2 == 0) {
        cout << "Error" << endl;
        goto flag4;
    }

    cin.clear();
    cin.ignore();
    cout << "key2 " << r2 << endl;

    seed(r1, r2);

    cout << "Decrypted text: ";
    for (int i = 0; i < str.length(); i++) {
        str[i] = cipher(crypt_str[i], key2);
        next_key();
    }
    cout << str << endl;

    return 0;
}

