#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define EPSILON 1e-9
double my_abs(double x) {
    return (x < 0) ? -x : x;
}
void jacobi_method(double **matrix, int n) {

    double **V = (double **)malloc(n * sizeof(double *));
    for (int i = 0; i < n; i++) {
        V[i] = (double *)malloc(n * sizeof(double));
        for (int j = 0; j < n; j++) {
            V[i][j] = (i == j) ? 1.0 : 0.0;
        }
    }


    int max_iter = 1000;
    double epsilon = 1e-10;

    for (int iter = 0; iter < max_iter; iter++) {

        int p = 0, q = 1;
        double max_val = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (my_abs(matrix[i][j]) > max_val) {
                    max_val = my_abs(matrix[i][j]);
                    p = i;
                    q = j;
                }
            }
        }


        if (max_val < epsilon) break;


        double theta = 0.5 * atan2(2 * matrix[p][q], matrix[q][q] - matrix[p][p]);
        double c = cos(theta);
        double s = sin(theta);

 
        for (int i = 0; i < n; i++) {
            if (i != p && i != q) {
                double ip = matrix[i][p];
                double iq = matrix[i][q];
                matrix[i][p] = c * ip - s * iq;
                matrix[p][i] = matrix[i][p];
                matrix[i][q] = c * iq + s * ip;
                matrix[q][i] = matrix[i][q];
            }


            double vi_p = V[i][p];
            double vi_q = V[i][q];
            V[i][p] = c * vi_p - s * vi_q;
            V[i][q] = c * vi_q + s * vi_p;
        }


        double pp = matrix[p][p];
        double qq = matrix[q][q];
        double pq = matrix[p][q];
        matrix[p][p] = c * c * pp - 2 * s * c * pq + s * s * qq;
        matrix[q][q] = s * s * pp + 2 * s * c * pq + c * c * qq;
        matrix[p][q] = matrix[q][p] = 0;
    }


    printf("Eigenvalues using Jacobi method:\n");
    for (int i = 0; i < n; i++) {
        printf("%lf\n", matrix[i][i]);
    }


    for (int i = 0; i < n; i++) {
        free(V[i]);
    }
    free(V);
}
int is_symmetric(double **matrix, int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (my_abs(matrix[i][j] - matrix[j][i]) > EPSILON) {
                return 0;
            }
        }
    }
    return 1;
}
void hessenberg_reduction(double **matrix, int n) {
    for (int k = 0; k < n - 2; k++) {
        for (int i = k + 2; i < n; i++) {
            if (my_abs(matrix[i][k]) > EPSILON) {

                double max_elem = 0;
                int pivot_row = i;
                for (int j = i; j < n; j++) {
                    if (my_abs(matrix[j][k]) > max_elem) {
                        max_elem = my_abs(matrix[j][k]);
                        pivot_row = j;
                    }
                }

                double x = matrix[k + 1][k];
                double y = matrix[pivot_row][k];
                double r = sqrt(x * x + y * y);
                
                if (r > EPSILON) {
                    double c = x / r;
                    double s = -y / r;
                    

                    for (int j = k; j < n; j++) {
                        double temp1 = c * matrix[k + 1][j] - s * matrix[pivot_row][j];
                        double temp2 = s * matrix[k + 1][j] + c * matrix[pivot_row][j];
                        matrix[k + 1][j] = temp1;
                        matrix[pivot_row][j] = temp2;
                    }
                    

                    for (int j = 0; j < n; j++) {
                        double temp1 = c * matrix[j][k + 1] - s * matrix[j][pivot_row];
                        double temp2 = s * matrix[j][k + 1] + c * matrix[j][pivot_row];
                        matrix[j][k + 1] = temp1;
                        matrix[j][pivot_row] = temp2;
                    }
                }
            }
        }
    }
}

void qr_algorithm(double **matrix, int n) {
    double *eigenvalues = (double *)malloc(n * sizeof(double));
    int max_iter = 10000;
    
    for (int iter = 0; iter < max_iter; iter++) {

        double shift = matrix[n-1][n-1];
        
        for (int i = 0; i < n; i++) {
            matrix[i][i] -= shift;
        }
        

        for (int k = 0; k < n - 1; k++) {
            double x = matrix[k][k];
            double y = matrix[k + 1][k];
            double r = sqrt(x * x + y * y);
            
            if (r > EPSILON) {
                double c = x / r;
                double s = -y / r;
                

                for (int j = k; j < n; j++) {
                    double temp1 = c * matrix[k][j] - s * matrix[k + 1][j];
                    double temp2 = s * matrix[k][j] + c * matrix[k + 1][j];
                    matrix[k][j] = temp1;
                    matrix[k + 1][j] = temp2;
                }
                

                for (int j = 0; j < n; j++) {
                    double temp1 = c * matrix[j][k] - s * matrix[j][k + 1];
                    double temp2 = s * matrix[j][k] + c * matrix[j][k + 1];
                    matrix[j][k] = temp1;
                    matrix[j][k + 1] = temp2;
                }
            }
        }
        

        for (int i = 0; i < n; i++) {
            matrix[i][i] += shift;
        }
        

        int converged = 1;
        for (int i = 1; i < n; i++) {
            if (my_abs(matrix[i][i-1]) > EPSILON) {
                converged = 0;
                break;
            }
        }
        
        if (converged) {
            printf("Converged after %d iterations\n", iter + 1);
            for (int i = 0; i < n; i++) {
                printf("Eigenvalue %d: %lf\n", i+1, matrix[i][i]);
            }
            free(eigenvalues);
            return;
        }
    }
    
    printf("Failed to converge after %d iterations\n", max_iter);
    free(eigenvalues);
}
int main() {
    int n;
    printf("Enter the order of the square matrix: ");
    scanf("%d", &n);

    double **matrix = (double **)malloc(n * sizeof(double *));
    for (int i = 0; i < n; i++) {
        matrix[i] = (double *)malloc(n * sizeof(double));
    }

    printf("Enter the elements of the matrix:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%lf", &matrix[i][j]);
        }
    }

    if (is_symmetric(matrix, n)) {
        printf("Matrix is symmetric. Using Jacobi method.\n");
        jacobi_method(matrix, n);
    } else {
        printf("Matrix is not symmetric. Using Hessenberg QR method.\n");
        hessenberg_reduction(matrix, n);
        qr_algorithm(matrix, n);
    }

    for (int i = 0; i < n; i++) {
        free(matrix[i]);
    }
    free(matrix);

    return 0;
}
