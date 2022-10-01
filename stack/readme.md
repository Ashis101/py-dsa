# stack

# underflow
-> when pop() or peek() called on empty stack

# overlow
-> when push() called on a full stack

# application of stack

- FUnction calls
- checking for balanced paranthesis
- reversing items
- infix to prefix/postfix
- evaluation of postfix/prefix
- stack span problem and its variations
- undo/redo or forward/backward

# Infix Prefix & Postfix

Infix: x+y
Postfix: xy+
prefix: +xy

# Advantages of Prefix & Postfix

* Do not require paranthesess,precedure rules and associativity rules

* Can be evaluated by writting a programme that traverse the given expression exactly once

  infix       Prefix        Postfix

x+y*z        +x*yz          xyz*+

(x+y)*z      *+xyz          xy+z*


steps for Postfix Conversion:-

x+y*z =>(x+(y*z))            (x+y)*z => ((x+y)*z)
      =>(x+(yz*))                    => ((xy+1)*z)
      =>xyz*+                        =>  xy+z*