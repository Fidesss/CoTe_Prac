<br>

# 🎢 [실패율](https://school.programmers.co.kr/learn/courses/30/lessons/42889) **[ Lv 1 ]**
<br>

## 📚 문제
![image](https://github.com/user-attachments/assets/7860fa1d-a13b-4c06-b285-8f57d3b8a360)
<br>

## 🗒️ 제한사항
![image](https://github.com/user-attachments/assets/c1c91a0c-1059-4ed0-b453-4043e0fadcd4)
<br>

## ⌨️ 입출력
![image](https://github.com/user-attachments/assets/b15d7840-7de6-4b76-9759-e0b813309a94)
<br>

## 💻 입출력 예 설명
![image](https://github.com/user-attachments/assets/91eacf71-1f39-4a88-9caa-18a0dd011e57)
<br>

<details>

  <summary> 
  
  ## 🎈 문제 풀이
  </summary>
  
## 🙈 문제에 대한 생각
> 처음에 단순히 문제에 접근하기 위해 각 인덱스와 실패율을 리스트에 넣고 문제 조건에 맞게 코드를 작성했으나 시간복잡도를 고려하지 못하여 실패
>
> 그 후 각 스테이지에 도전하는 사람들의 수를 리스트로 저장
>
> 실패율을 딕셔너리를 사용해 저장

</br>

## 📄 중요 로직
> 각 스테이지에 도전하는 사람들을 저장하는 challenger 리스트를 스테이지 수 + 2 만큼의 크기를 잡는다.
>
> > 이렇게 하는 이유
> >
> > 0번 인덱스를 사용하지 않으며 마지막 스테이지를 클리어한 사람 수 까지도 저장하기 위함
>
> 실패율을 저장하는 딕셔너리인 fails에서 key 값은 스테이지를 클리어하지 못한 사람, value 값은 실패율이다.
>
> fails에 각 스테이지 실패율을 저장
>
> 실패율을 기준으로 내림차순으로 정렬

</br>

## 📜 전체 로직
> 1. challenger 리스트 크기를 N + 2 만큼 잡고 각 리스트의 원소를 0 으로 초기화
> 2. 반복문을 수행하며 각 스테이지의 도전하고있는 사람을 찾을 때마다 challenger 리스트에 1을 더함
> 3. 실패율을 저장하는 fails 딕셔너리를 선언
> 4. 스테이지에 도전하는 전체 사람수를 total이라는 변수에 저장
> 5. 인덱스를 1부터 시작하여 N+1까지 반복문을 수행
> > 도전하는 사람의 수를 저장한 challenger에 도전하는 사람이 없을때 실패율의 value에 0을 저장
> > 도전하는 사람이 있을경우 fails의 value에 그 스테이지의 실패율을 저장
> > total의 수에서 그 스테이지의 사람수를 뺀다.
> 6. fails 딕셔너리에서 value값을 기준으로 내림차순
> 7. 답의 리스트를 반환

</br>

## 🪄 참고 자료
> ### 코딩테스트 합격자 되기 파이썬 편

</details>
