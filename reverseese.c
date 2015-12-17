int main(int arg0) {
    esp = (esp & 0xfffffff0) - 112;
    read_80_bytes(esp + 20);
    atoi(esp + 20);
    if (*(esp + 104) > 40) {
            eax = exit(0x0);
    }
    else {
            open("/home/xorflag/key", 0x0);
            stack[2046] = *(esp + 104);
            eax = *(esp + 100);
            read(eax, esp + 20, stack[2046]);
            eax = *(esp + 100);
            close(eax);
            open("/home/xorflag/flag", 0x0);
            eax = *(esp + 104);
            edx = *(esp + 104);
            stack[2046] = eax;
            eax = *(esp + 100);
            read(eax, edx + esp + 20, stack[2046]);
            eax = *(esp + 100);
            close(eax);
            while (*(esp + 108) < *(esp + 104)) {
                    *(int8_t *)(*(esp + 108) + esp + 20) = *(int8_t *)(esp + 20 + *(esp + 104) + *(esp + 108)) & 0xff ^ *(int8_t *)(*(esp + 108) + esp + 20) & 0xff;
            }
            eax = *(esp + 104);
            eax = write(0x1, esp + 20, eax);
    }
    return eax;
}



void read_80_bytes(int arg0) {
    for (var_C = 0x0; var_C <= 799; var_C = var_C + 1) {
            read(0x0, arg0 + var_C, 0x1);
            if ((*(int8_t *)(arg0 + var_C) & 0xff) == 0xa) {
                break;
            }
    }
    return;
}
