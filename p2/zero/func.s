.686
.model flat,C ;
public C next_key ;
public C cipher
.code ;
next_key proc _arr : word, _n ;
mov EAX, _n ;

@@start: ;
rct AL, 1
ret
next_key endp

cipher proc _arr : word, _n : word, _a;
mov EAX, _a ;
mov EBX, _n ;
@@start: ;
xor EBX, EAX ;
cipher endp
END
