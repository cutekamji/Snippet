# 리스트 원소 최빈값 구하기

from collections import Counter

# 원소별 빈도 출력
# 딕셔너리 안에 튜플(원소, 개수) 형식
Counter(list)

# 상위 n 개의 원소 출력
# (원소, 빈도) 튜플 형식
Counter(list).most_common(n)

# 최빈값 원소가 여러개일 경우 최빈값인 모든 원소 찾기
# 이 코드를 응용하여 원소가 n번 등장하는 모든 원소 찾기도 가능
mode = []
for e in Counter(list).keys():
  if Counter(list)[e] == Counter(list).most_common(1)[0][1]:
    mode.append(e)
