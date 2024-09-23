<br>

# 🎢 [24511 queuestack](http://www.acmicpc.net/problem/24511) <img height="27px" width="27px" src="https://static.solved.ac/tier_small/8.svg"/>
<br>

## 📚 문제
![image](https://github.com/user-attachments/assets/535e6c5b-62a2-453e-9e9e-356e90aec952)
<br>

## ⌨️ 입력
![image](https://github.com/user-attachments/assets/53593f3a-4e01-48c4-b953-00ebba68fbe8)
<br>

## 🏃‍♂️ 출력
> 수열 C 의 원소를 차례대로 queuestack에 삽입했을 때의 리턴값을 공백으로 구분하여 출력한다.

<br>
<details>

  <summary> 
  
  ## 🎈 문제 풀이
  </summary>
  
## 🙈 문제에 대한 생각
> 스택의 경우 push연산과 pop연산을 했을 때 push한 값이 pop이 되는것 -> 사실상 없는것과 마찬가지
>
> 큐는 이미 초기에 저장되어있는 값이 pop을 했을때 나온다.
>
> 문제를 잘 살펴본 결과 출력되는 값은 결국 마지막 큐에서 pop되는 값임을 알아냄
>
> 각 큐를 하나의 큐로 생각하고 deque에 초기값을 삽입 (여기서 큐를 deque를 사용)
>
> 다섯째 줄에 삽입할 원소를 담고있는 수열 C를 차례대로 deque의 왼쪽에 삽입

</br>

## 📄 중요 로직
> 1. 0일경우 초기값이 들어있는 리스트에서 지금 인덱스에 저장되어있는 값에 접근한다.
> 2. 그 값을 deque에 저장한다.
> 3. 반복문을 수열 C의 길이 만큼 돌린다.
> 4. 수열 C의 값이 저장되어있는 리스트를 인덱스 0부터 차례대로 접근하여 큐의 왼쪽에 삽입한다.
> 5. 큐에서 pop연산을 수행하여 출력한다.

</br>

## 📜 전체 로직
> 1. queuestack을 구성하는 자료구조의 개수 입력 받을 변수 선언
> 2. 0일때 큐, 스택일때 1인 수열을 입력받을 리스트 선언 (각각을 공백한 칸 으로 구분)
> 3. queuestack에 저장할 초기값을 입력받을 리스트 선언 (각각을 공백한 칸 으로 구분)
> 4. 삽입할 수열의 길이를 입력받을 변수 선언
> 5. 삽입할 수열을 입력받고 저장할 리스트 선언 (각각을 공백한 칸 으로 구분)
> 6. 위의 중요로직 수행

</details>
<!-- ## 🪄 참고 자료 --!>
