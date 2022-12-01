	.file	"func.c"
	.text
	.globl	key
	.bss
	.type	key, @object
	.size	key, 1
key:
	.zero	1
	.text
	.globl	get_key
	.type	get_key, @function
get_key:
.LFB0:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movzbl	key(%rip), %eax
	movzbl	%al, %eax
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	get_key, .-get_key
	.globl	next_key
	.type	next_key, @function
next_key:
.LFB1:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movb	$1, -1(%rbp)
	movzbl	key(%rip), %eax
	movzbl	%al, %edx
	movzbl	-1(%rbp), %eax
	movl	%eax, %ecx
	sarl	%cl, %edx
	movl	%edx, %eax
	movl	%eax, %edi
	movzbl	key(%rip), %eax
	movzbl	%al, %esi
	movzbl	-1(%rbp), %eax
	movl	$8, %edx
	subl	%eax, %edx
	movl	%esi, %eax
	movl	%edx, %ecx
	sall	%cl, %eax
	orl	%edi, %eax
	movb	%al, key(%rip)
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE1:
	.size	next_key, .-next_key
	.globl	seed
	.type	seed, @function
seed:
.LFB2:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movl	%edi, %eax
	movb	%al, -4(%rbp)
	movzbl	-4(%rbp), %eax
	movb	%al, key(%rip)
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE2:
	.size	seed, .-seed
	.globl	cipher
	.type	cipher, @function
cipher:
.LFB3:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movl	%edi, %edx
	movl	%esi, %eax
	movb	%dl, -4(%rbp)
	movb	%al, -8(%rbp)
	movzbl	-4(%rbp), %eax
	xorb	-8(%rbp), %al
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE3:
	.size	cipher, .-cipher
	.ident	"GCC: (GNU) 12.2.0"
	.section	.note.GNU-stack,"",@progbits
