'''Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.'''
  
#include<stdio.h>
#include<stdlib.h>
int main() {
    int hh, mm, ss ;
    char t12[3];
    scanf("%d:%d:%d%s", &hh, &mm, &ss, t12) ;
        
    if (strcmp(t12,"PM")==0 && hh!=12) hh += 12 ;
    if (strcmp(t12,"AM")==0 && hh==12) hh = 0 ;
        
    printf("%02d:%02d:%02d", hh, mm, ss) ;
    return 0;
}
