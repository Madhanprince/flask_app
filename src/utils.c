#include <stdio.h>
#include <time.h>
#include "utils.h"

void print_current_time() {
    time_t now = time(NULL);
    struct tm *t = localtime(&now);
    printf("Current time: %02d:%02d:%02d\n", t->tm_hour, t->tm_min, t->tm_sec);
}
