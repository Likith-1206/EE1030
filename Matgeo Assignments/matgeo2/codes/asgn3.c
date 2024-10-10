#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "libs/matfun.h"
#include "libs/geofun.h"

// Function to generate points on the parabola y^2 = x
void generate_parabola_points(double *x_values, int n, const char *filename) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        exit(1);
    }

    // Loop through the provided x values and calculate corresponding y values
    for (int i = 0; i < n; i++) {
        double x = x_values[i];
        double y = sqrt(x);    // Calculating positive root (y^2 = x)
        double neg_y = -y;      // Calculating negative root (y^2 = x)

        // Writing points to file
        fprintf(file, "For x = %.6f: (%.6f, %.6f) and (%.6f, %.6f)\n", x, x, y, x, neg_y);
    }

    fclose(file);
}

// Function to generate a series of points on the parabola for plotting
void generate_parabola_series(double x_start, double x_end, double step, const char *filename) {
    FILE *file = fopen(filename, "a");
    if (file == NULL) {
        printf("Error opening file!\n");
        exit(1);
    }

    // Generate points between x_start and x_end with the given step
    for (double x = x_start; x <= x_end; x += step) {
        double y = sqrt(x);
        double neg_y = -y;

        // Write each point to the file for plotting
        fprintf(file, "Parabola point for x = %.6f: (%.6f, %.6f)\n", x, x, y);
        fprintf(file, "Parabola point for x = %.6f: (%.6f, %.6f)\n", x, x, neg_y);
    }

    fclose(file);
}

int main() {
    // Define the specific x-values for intersections and parabola generation
    double x_values[] = {0.25, 1.0};  // For intersections with x = 0.25 and x = 1.0
    int n = sizeof(x_values) / sizeof(x_values[0]); // Calculate the size of the x_values array

    // Generate and write the points of intersection
    generate_parabola_points(x_values, n, "asgn3.txt");

    // Generate and write more points on the parabola for plotting
    double x_start = 0.0, x_end = 2.0, step = 0.1;  // Generate points from x=0 to x=2 with step 0.1
    generate_parabola_series(x_start, x_end, step, "asgn3.txt");

    printf("Points of intersection and parabola points have been written to asgn3.txt\n");
    return 0;
}

