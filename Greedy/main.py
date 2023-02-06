# 예제 3-1
n = 1260
count = 0

coin_types = [500, 100, 50, 10]

# 화폐의 종류(K)만큼 반복 수행... 시간 복잡도는 O(K)
for coin in coin_types:
    count += n // coin
    n %= coin

print(count)