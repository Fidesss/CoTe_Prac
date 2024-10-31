<br>

# 🛠️ [1106 호텔](http://www.acmicpc.net/problem/1106) <img height="27px" width="27px" src="https://static.solved.ac/tier_small/12.svg"/>
<br>

## 📖 문제
![image](https://github.com/user-attachments/assets/67f36f4e-d170-4ba4-a436-2a43a03ce484)

<br><br>

## ⌨️ 입력
![image](https://github.com/user-attachments/assets/d533775e-e3f4-4451-95ba-d33e7d6780c4)

<br>

## 💻 출력
>첫째 줄에 문제의 정답을 출력한다.
</br>


## 🗒️예제입력
![image](https://github.com/user-attachments/assets/aea342a8-a28b-4506-8b30-0860d59bbef4)
![image](https://github.com/user-attachments/assets/f52e735f-45bb-465d-bdce-3cc45e0c44f6)


<br><br>

<details>

  <summary> 
  
  ## 🎈 참고
  </summary>
  
## 🙈 생각
> knapsack문제를 생각
> 한번 선택한 도시를 다시 선택할 수 있다는 것에 집중
> dp리스트에 고객을 적어도 C명 늘린다고 했을때 최소비용을 저장
> dp[i] = 적어도 i명의 고객을 늘리기 위한 최소 비용


## 📄중요 로직
> 1. dp[a]에는 적어도 a명의 고객을 늘이기 위한 최소 비용이 저장된다.
> 2. dp[a]의 비용이 dp[a+1]의 비용보다 클 수 있음
> 3. 그래서 출력할 때 일정 크기의 dp를 모두 구한 뒤 적어도 C이상의 고객을 얻는 비용 중 최소 값을 반환 (dp[C:])
> 4. 그래서 이것을 고려하기 위해 얻고자 하는 고객 수 보다 한 도시에서 얻을 수 있는 최대 고객의 수인 100만큼 크게 만들었음.

</details>

<!-- ### 전체 로직 --!>
 
<!-- ### 코드 진행 --!>
<br>

<!-- ## 🪄 참고 자료 --!>

<br><br>
