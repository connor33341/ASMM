section .data:
    msg db "hello, world!", 0xa ; message followed by newline
    len eq $ - msg ; calculate length of message


section .text:
    global _start 


_start:
    mov eax, 4   ; syscall number for sys_write
    mov ebx, 1   ; file descriptor 1  stdout 
    mov ecx, msg  ; pointer to message
    mov edx, len  ; message length
    int 0x80  ; call kernel

    mov eax, 1  ; syscall number for sys_exit
    xor ebx, ebx  ; exit code 0
    int 0x80  ; call kernel