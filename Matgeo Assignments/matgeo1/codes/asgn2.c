#include <stdio.h>
#include <math.h>

// Struct to represent 2D points
typedef struct {
    double x;
    double y;
} Point;

// Function to calculate trisection points P and Q
void calculateTrisectionPoints(Point A, Point B, Point* P, Point* Q) {
    // Trisection points formula
    P->x = (2*A.x + B.x) / 3.0;
    P->y = (2*A.y + B.y) / 3.0;

    Q->x = (A.x + 2*B.x) / 3.0;
    Q->y = (A.y + 2*B.y) / 3.0;
}

int main() {
    Point A = {7, -2};
    Point B = {1, -5};
    Point P, Q;

    // Calculate the points P and Q
    calculateTrisectionPoints(A, B, &P, &Q);

    // Output the points P and Q
    printf("P = (%.2f, %.2f)\n", P.x, P.y);
    printf("Q = (%.2f, %.2f)\n", Q.x, Q.y);

    // Return Q.y so that Python can use it
    return 0;
}

