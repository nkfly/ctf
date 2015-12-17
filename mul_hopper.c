int main(int arg0, int arg1, int arg2, int arg3) {
    esp = (esp & 0xfffffff0) - 0x340;
    eax = *stdout@@GLIBC_2.0;
    setvbuf(eax, 0x0, 0x2, 0x0);
    printf("Number of row: ");
    __isoc99_scanf(0x8048860, esp + 0x14);
    printf(0x8048863);
    __isoc99_scanf(0x8048860, esp + 0x10);
    if (*(esp + 0x10) * *(esp + 0x14) > 0xc8) {
            puts("Size too large!");
            eax = exit(0x0);
    }
    else {
            printf("Row: ");
            do {
                    if (*(esp + 0x33c) >= *(esp + 0x14)) {
                        break;
                    }
                    eax = *(esp + 0x33c);
                    __isoc99_scanf(0x8048860, (eax << 0x2) + 0x804a380);
            } while (*(*(esp + 0x33c) * 0x4 + 0x804a380) != 0x0);
            printf("Column: ");
            do {
                    if (*(esp + 0x33c) >= *(esp + 0x10)) {
                        break;
                    }
                    eax = *(esp + 0x33c);
                    __isoc99_scanf(0x8048860, (eax << 0x2) + 0x804a060);
            } while (*(*(esp + 0x33c) * 0x4 + 0x804a060) != 0x0);
            while (*(esp + 0x33c) < *(esp + 0x14)) {
                    while (*(esp + 0x338) < *(esp + 0x10)) {
                            *(esp + (*(esp + 0x10) * *(esp + 0x33c) + *(esp + 0x338)) * 0x4 + 0x18) = *(*(esp + 0x338) * 0x4 + 0x804a060) * *(*(esp + 0x33c) * 0x4 + 0x804a380);
                    }
            }
            while (*(esp + 0x33c) < *(esp + 0x14)) {
                    while (*(esp + 0x338) < *(esp + 0x10)) {
                            if ((*(esp + 0x338) + *(esp + 0x33c) & 0x1) == 0x0) {
                                    edx = *(esp + 0x10) * *(esp + 0x33c);
                                    eax = *(esp + 0x338);
                                    eax = *(esp + (eax + edx) * 0x4 + 0x18);
                                    printf(0x8048895, eax);
                            }
                            else {
                                    printf(0x8048899);
                            }
                    }
                    puts(0x804889d);
            }
            eax = 0x0;
    }
    return eax;
}


int __cdecl main(int argc, const char **argv, const char **envp)
{
  unsigned int v4; // [sp+10h] [bp-330h]@1
  unsigned int v5; // [sp+14h] [bp-32Ch]@1
  int v6; // [sp+18h] [bp-328h]@16
  unsigned int j; // [sp+338h] [bp-8h]@15
  unsigned int i; // [sp+33Ch] [bp-4h]@4

  setvbuf(stdout, 0, 2, 0);
  printf("Number of row: ");
  __isoc99_scanf("%u", &v5);
  printf("Number of column: ");
  __isoc99_scanf("%u", &v4);
  if ( v5 * v4 > 0xC8 )
  {
    puts("Size too large!");
    exit(0);
  }
  printf("Row: ");
  for ( i = 0; i < v5; ++i )
  {
    __isoc99_scanf("%u", 4 * i + 0x804a380);
    if ( !a[i] )
    {
      v5 = i;
      break;
    }
  }
  printf("Column: ");
  for ( i = 0; i < v4; ++i )
  {
    __isoc99_scanf("%u", 4 * i + 0x804a060);
    if ( !b[i] )
    {
      v4 = i;
      break;
    }
  }
  for ( i = 0; i < v5; ++i )
  {
    for ( j = 0; j < v4; ++j )
      *(&v6 + j + i * v4) = a[i] * b[j];
  }
  for ( i = 0; i < v5; ++i )
  {
    for ( j = 0; j < v4; ++j )
    {
      if ( ((_BYTE)i + (_BYTE)j) & 1 )
        printf(" . ");
      else
        printf("%3d", *(&v6 + i * v4 + j));
    }
    puts(&byte_804889D);
  }
  return 0;
}
