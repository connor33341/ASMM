section .data:
        msg db "Hello, World!", 0xA ; Message followed by newline
        len equ $ - msg ; Calculate length of message


section .text:
        global _start


_start:
        mov EAX, 4  ; syscall number for sys_write
        mov EBX, 1  ; file descriptor 1 (stdout)
        mov ECX, MSG ; pointer to message
        mov EDX, LEN ; message length
        int 0x80 ; call kernel

        mov EAX, 1 ; syscall number for sys_exit
        xor EBX, EBX ; exit code 0
        int 0x80 ; call kernel