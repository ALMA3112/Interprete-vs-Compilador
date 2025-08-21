#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <sys/resource.h>

double now_seconds() {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return tv.tv_sec + tv.tv_usec * 1e-6;
}

long long recursive_sum(long long *arr, int n) {
    if (n == 0) return 0;
    return arr[n - 1] + recursive_sum(arr, n - 1);
}

int main() {
    int powers = 6; // 100, 1k, 10k, 100k, 1M, 10M
    for (int p = 0; p < powers; ++p) {
        int n = 100;
        for (int i = 0; i < p; ++i) n *= 10;

        long long *arr = (long long*)malloc(sizeof(long long) * n);
        if (!arr) {
            fprintf(stderr, "Allocation failed for n=%d\n", n);
            return 1;
        }
        for (int i = 0; i < n; ++i) arr[i] = i;

        double t0 = now_seconds();
        long long sum = recursive_sum(arr, n);
        double t1 = now_seconds();

        struct rusage usage;
        getrusage(RUSAGE_SELF, &usage);
        double peak_mb = (double)usage.ru_maxrss / 1024.0;

        double elapsed = t1 - t0;
        printf("n=%d  Tiempo = %.6f s\n", n, elapsed);
        printf("n=%d  Memoria = %.6f MB\n", n, peak_mb);

        free(arr);
    }
    return 0;
}
