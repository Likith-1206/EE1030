#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "libs/matfun.h"
#include "libs/geofun.h"  // Include geofun.h for geometric operations

// Function to calculate trisection points P and Q
void calculate_trisection(double **A, double **B, double **P, double **Q) {
    // Trisection formulas
    P[0][0] = (2 * B[0][0] + A[0][0]) / 3;  // P (1:2)
    P[1][0] = (2 * B[1][0] + A[1][0]) / 3;

    Q[0][0] = (B[0][0] + 2 * A[0][0]) / 3;  // Q (2:1)
    Q[1][0] = (B[1][0] + 2 * A[1][0]) / 3;
}

// Function to generate points of trisection and write them to a file
void point_gen(double **A, double **B, const char *filename) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        printf("Error opening file.\n");
        return;
    }

    // Allocate memory for trisection points
    double **P = createMat(2, 1);
    double **Q = createMat(2, 1);

    // Calculate trisection points
    calculate_trisection(A, B, P, Q);

    // Write the points to the file
    fprintf(file, "Point A: (%lf, %lf)\n", A[0][0], A[1][0]);
    fprintf(file, "Point B: (%lf, %lf)\n", B[0][0], B[1][0]);
    fprintf(file, "Trisection Point P (1:2): (%lf, %lf)\n", P[0][0], P[1][0]);
    fprintf(file, "Trisection Point Q (2:1): (%lf, %lf)\n", Q[0][0], Q[1][0]);

    // Close the file
    fclose(file);

    // Free allocated memory
    freeMat(P, 2);
    freeMat(Q, 2);
}

int main() {
    // Initialize points A(7, -2) and B(1, -5)
    double **A = createMat(2, 1);
    double **B = createMat(2, 1);

    A[0][0] = 7;
    A[1][0] = -2;
    B[0][0] = 1;
    B[1][0] = -5;

    // Generate trisection points and save them to asgn2.dat
    point_gen(A, B, "asgn2.dat");

    // Free the allocated memory for A and B
    freeMat(A, 2);
    freeMat(B, 2);

    return 0;
}

