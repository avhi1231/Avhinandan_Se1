#include <stdio.h>

void main() {
  char s1[10] = "Ram", s2[30] = "sita", s3[10] = "Deep";
  int result;

  // comparing strings str1 and str2
  result = strcmp(s1, s2);
  printf("strcmp(s1, s2) = %d\n", result);

  // comparing strings str1 and str3
  result = strcmp(s1, s3);
  printf("strcmp(s1, s3) = %d\n", result);

}
