# BOJ 26772 : Poziome serca
# https://www.acmicpc.net/problem/26772


import sys
a = int(sys.stdin.readline().rstrip())

msg = ''' @@@   @@@ 
@   @ @   @
@    @    @
@         @
 @       @ 
  @     @  
   @   @   
    @ @    
     @     '''

for m in msg.split('\n'):
    for _ in range(a):
        print(m, end=" ")
    print()