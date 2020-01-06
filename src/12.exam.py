# https://wikidocs.net/42527

'''
Q1. 다음 코드의 결괏값은 무엇일까?

a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
'''

print('shirt')

'''
Q2. while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
'''

num = 1
sum_of_num = 0

while num <= 1000:
  if num % 3 == 0:
    sum_of_num += num
  num += 1

print(sum_of_num)

'''
Q3. while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.

*
**
***
****
*****
'''

num = 1

while num <= 5:
  print('*' * num)
  num += 1

'''
Q4. for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
'''

for i in range(1, 101):
  print(i, end=' ')
print()

'''
Q5. A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.

[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

for문을 사용하여 A 학급의 평균 점수를 구해 보자.
'''

a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum_of_score = 0
length = len(a)

for score in a:
  sum_of_score += score

print('average: %f' % (sum_of_score / length))

'''
Q6. 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.

numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)

위 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.
'''

numbers = [1, 2, 3, 4, 5]
result = [x * 2 for x in numbers]
print(result)