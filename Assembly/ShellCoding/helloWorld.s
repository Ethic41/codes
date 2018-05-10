BITS 32 ; Tell nasm that this is a 32-bit code

call mark_below ; Call below the string to instructions
db "hello, World!", 0x0a, 0x0d ; String with newline and carriage return


mark_below:
;ssize_t write(int fd, const void, sizee_t count);
pop ecx ; pop the return address(string ptr) into ecx
mov eax, 4 ; since write is syscal #4
mov ebx, 1 ; since stdout is 1
mov edx, 15 ; the length of the string
int 0x80 ; tell the kernel to make syscall

;void _exit(int status);

mov eax, 1; exit is syscall #1
mov ebx, 0; exit is syscall #2
int 0x80; make syscall: exit(0)




;End of code
