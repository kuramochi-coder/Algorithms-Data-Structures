#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int numberOfTaps, i;
    float totalFlowRate = 0;
    scanf("%d", &numberOfTaps);
    
    for (i = 0; i < numberOfTaps; i++)
    {
        float totalTimeToFill;
        scanf("%f", &totalTimeToFill);
        totalFlowRate += pow(totalTimeToFill, -1);
    }
    
    int totalTime;
    
    totalTime = round((pow(totalFlowRate, -1) * 60));
    printf("%d", totalTime);
    
    return 0;
}

