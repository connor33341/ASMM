; What main.asmm repersents

section .data
    msg db "Hello, World!", 0xA  ; The message string followed by a newline
    len equ $ - msg              ; Calculate the length of the message

section .text
    global _start                ; Entry point

_start:
    ; syscall: write (sys_write)
    mov eax, 4      ; syscall number for sys_write (Linux x86)
    mov ebx, 1      ; file descriptor 1 (stdout)
    mov ecx, msg    ; pointer to message
    mov edx, len    ; message length
    int 0x80        ; call kernel

    ; syscall: exit (sys_exit)
    mov eax, 1      ; syscall number for sys_exit (Linux x86)
    xor ebx, ebx    ; exit code 0
    int 0x80        ; call kernel
