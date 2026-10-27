#include <iostream>
int main() {
    int x = 1, y = 2, z = 0;
    z = z + 2 * (++x) + 3 * y, ++y;
    std::cout << "x=" << x << " y=" << y << " z=" << z << std::endl;
    return 0;
}
