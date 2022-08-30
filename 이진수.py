T = int(input())

for i in range(T):
  n = bin(int(input()))[2:] # bin()함수: 10진수 -> 2진수
                            # ob1010과 같은 값이 나와서, 숫자만 사용하기 위해 슬라이싱으로 [2:] 잘라줌
  for j in range(len(n)):
    if n[-j-1] == "1":         # 위치가 낮은 것부터 출력
      print(j, end=' ')      # 1의 위치를 공백으로 구분해서 줄 하나에 출력
