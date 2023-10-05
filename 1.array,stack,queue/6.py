# Вам даны два непустых списка А и В одинаковой длины. В списке А целые числа (все разные), представляющие рыб в реке, рыба на позиции имеет размер A[i]. 
# В списке В лежат 0 и 1, показывающие направление движения (0 --- влево, 1 --- вправо). Рыбы движутся с одинаковой скоростью. 
# Если две рыбы движутся по направлению друг к другу, и между ними никого нет (живого), то в какой-то момент они встретятся, и большая по размеру съест меньшую, продолжая двигаться в своем направлении.
# Скажите, сколько рыб останется вживых.
# Пример:
# A[0] = 4 B[0] = 0
# A[1] = 3 B[1] = 1
# A[2] = 2 B[2] = 0
# A[3] = 1 B[3] = 0
# A[4] = 5 B[4] = 1
# Изначально все рыбы живы. Затем рыба с позиции 1 встречается с рыбой позиции 2 и съедает ее. После этого она  встречается с рыбой, которая изначально была на позиции 3, и съедает ее тоже. 
# После чего рыба оказывается. что рыба 0 продолжает двигаться влево, а рыбы 1 и 4 движутся вправо (с одинаковой скоростью, так что никогда не встретятся). Таким образом, вживых осталось три рыбы.
# Sample Input:
# 4 3 2 1 5
# 0 1 0 0 1
# Sample Output:
# 3

def countsurvivingfish(A, B):
    stack = []
    survivingfish = 0

    for i in range(len(A)):
        if B[i] == 1:
            stack.append(A[i])
        else:
            while len(stack) > 0:
                if stack[-1] > A[i]:
                    break
                else:
                    stack.pop()
            else:
                survivingfish += 1

    survivingfish += len(stack)

    return survivingfish


A = list(map(int,input().split()))
B = list(map(int,input().split()))
result = countsurvivingfish(A, B)
print(result)