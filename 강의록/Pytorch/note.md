# [Pytorch] 강의록

---
# 키워드
* 네트워크 구현
* 데이터 로딩
* 프로젝트 구조 잡기
* 로깅
* Multi GPU


---
# 1.  Introduction to PyTorch
- 밑바닥부터 딥러닝 코드 짜기? [책](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=256067157&start=slayer)
- 딥러닝 프레임워크
  - 텐서플로
  - 파이토치 
- 우리는 파이토치를 쓰자.
- 계산 그래프 (Computational Graph)
  - Define and Rune
    - 그래프를 먼저 정의
  - Define by Run
    - 실행을 하면서 그래프를 생성
- Pytorch
  - 학회, 논문에 강점
  - **즉시 확인 가능**
  - **Numpy + AutoGrad + Function **
  - Multi GPU
- Tensorflow
  - 프로덕션에 강점


# 2. PyTorch Basics
- AutoGrad
  - # AutoGrad
```
w = torch.tensor(2.0, requires_grad=True)
y = w**2
z = 10*y + 25
z.backward()
w.grad

> z.backward() 를 통해 오차역전파를 계산
> w.grad 를 통해 z 에 대한 w 그레디언트 추출
```








# 3. Project Structure

# 4. AutoGrad & Optimizer

# 5. Pytorch Dataset & Dataloader

# 6. 모델 불러오기

# 7. Monitoring tools for PyTorch

# 8. Muti-GPU

# 9. Hyperparameter Tuning

# 10. PyTorch Troubleshooting

---


---
# 생각해볼점
- AutoGrad 작동 방식 ? 
- 