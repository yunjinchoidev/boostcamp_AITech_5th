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
```
w = torch.tensor(2.0, requires_grad=True)
y = w**2
z = 10*y + 25
z.backward()
w.grad

> z.backward() 를 통해 오차역전파를 계산
> w.grad 를 통해 z 에 대한 w 그레디언트 추출
```

- 최대가능도 추정법
  - 모수
    - 모수는 모집단의 특성(모평균,모분산 등..)을 나타내는 값으로, 이 값을 모집단을 전수조사해야만 알수있는 값이다. 그러나 실질적으로 모집단의 크기와 범위가 너무 방대하기에 전수조사를 실지하지 않고 표본조사를 하는데 표본평균,표본분산 등으로 모평균, 모분산등을 추정할수가 있다.








# 3. Project Structure
- 언제까지 코랩쓸래? 
- 템플릿을 쓰자.
- 템플릿
  - 실행, 데이터, 모델,  설정, 로깅, 지표, 유틸리티
  - [링크](https://github.com/victoresque/pytorch-template)
  - **템플릿 구조를 면밀하게 분석하는 것을 해보시라.**


---
# 4. AutoGrad & Optimizer
- 논문을 구현해봅시다.
- 딥러닝 -> layer 쌓기 -> 레고 블럭 쌓기
- 4요소
  - input
  - output
  - forward
  - backward




---

# 5. Pytorch Dataset & Dataloader
- 모델도 중요하지만, 데이터를 어떻게 잘 다루느냐도 중요하다.
  - 엄청나게 많은 데이터
- **Pytorch Dataset**
  - 먼저 데이터를 텐서로 바꾸고 DataLoder 로 모델에 먹이기
- **CustomDataset**
  - CustomDataset을 정의 하기 위해서 3개의 메소드를 반드시 정의해야 한다.
    - init, len, getitem
    - utils.data.Dataset 상속
- DataLoder
  - CustomDataset, 기타 옵션으로 실제 데이터에 적용하면 된다.
  - 옵션
    - 미니배치 사이즈
    - ... 많다.
  - 코드를 뜯어보시라.


---
# 6. 모델 불러오기
- 상황
  - 이 말인 즉슨 우리는 실제 라벨과 예측 라벨의 오차 함수의 그레디언트를 계산하고 오차역전파를 계산하여 W 가중치 텐서를 업데이트 시켰다. (공부를 했다. 경험을 했다. 수련을 했다.)
  - 우리는 이 결과를 전달하려 한다.
- model.save() 
- 저장법 2가지
  - 파라메터만 저장
  - 모델형테 + 파라메터 저장




---
# 7. Monitoring tools for PyTorch
- 체크포인트
  - 학습의 중간 결과를 저장
  - earlystopping 
  - loss, metric
  - Earlystopping : 조기 종료

- Loggin
  - Logging이란, 학습이 진행되면서 주요하다고 생각되는 지표들이나 학습의 상태 등 관련된 정보들을 기록하는 것

- Tensorboard
- Tensorboard는 TensorFlow의 프로젝트로 만들어진 시각화 도구로 학습 그래프, Metric, 학습 결과의 시각화를 지원

- Weight, Biases
  - 머신러닝 실험을 원활하게 지원하기 위한 상용 도구로써, 협업, code versioning, 실험 결과 기록 등의 기능을 제공하는 시각화 툴
---
# 8. Muti-GPU




---

# 9. Hyperparameter Tuning
- 학습률(Learning rate)
- 최적화 함수(Optimizer)
- 손실 함수(Loss Fucnction)
-  


---

# 10. PyTorch Troubleshooting




---


---
# 생각해볼점
- AutoGrad 작동 방식 ? 
- 