# BOJ 1978 : 소수 찾기
# https://www.acmicpc.net/problem/19778


import sys; input = sys.stdin.readline
from typing import List

def solution(Li: List[int]) -> int : 
    def isPrime(N: int) -> bool : 
        if N == 1 : return False
        for i in range(2, int(N**0.5)+1) : 
            if N % i == 0 : return False
        return True
     
    cnt = 0
    for num in Li : 
        if isPrime(num) : cnt += 1    

    return cnt

if __name__ == "__main__" : 
    _ = input()
    Li = list(map(int, input().split()))

    print(solution(Li))