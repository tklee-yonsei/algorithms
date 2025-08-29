# Insertion Sort vs Selection Sort vs Shell Sort 비교

이 프로젝트는 세 가지 기본 정렬 알고리즘의 성능과 동작을 시각적으로 비교하는 애니메이션을 제공합니다.

## 📁 프로젝트 구조

```
lec02/06_ins_sel_shell/
├── comprehensive_three_way_comparison.py  # 종합 비교 애니메이션
├── speed_comparison_animation.py          # 속도 비교 애니메이션
├── create_all_animations.py               # 모든 애니메이션 생성
├── complexity_analysis.md                 # 복잡도 분석 문서
├── README.md                              # 이 파일
└── img/                                   # 생성된 애니메이션 파일들
    ├── comprehensive_three_way_comparison.gif
    └── speed_comparison.gif
```

## 🎯 주요 기능

### 1. 종합 비교 애니메이션 (`comprehensive_three_way_comparison.gif`)

- **4가지 데이터 케이스**:

  - Random Array (랜덤 배열)
  - Nearly Sorted (거의 정렬된 배열)
  - Reversed Array (역순 배열)
  - Few Unique (중복이 많은 배열)

- **3개 정렬 알고리즘**:

  - Selection Sort (선택 정렬)
  - Insertion Sort (삽입 정렬)
  - Shell Sort (셸 정렬)

- **총 12개의 그림**: 4개 케이스 × 3개 알고리즘

### 2. 속도 비교 애니메이션 (`speed_comparison.gif`)

- 다양한 배열 크기에서의 실행 시간 비교
- 막대 그래프와 선 그래프로 시각화
- 실제 성능 측정 결과

## 🚀 실행 방법

### 모든 애니메이션 생성

```bash
cd lec02/06_ins_sel_shell
python create_all_animations.py
```

### 개별 애니메이션 생성

#### 종합 비교 애니메이션

```bash
python comprehensive_three_way_comparison.py
```

#### 속도 비교 애니메이션

```bash
python speed_comparison_animation.py
```

## 📊 알고리즘 비교 요약

| 특성                   | Selection Sort | Insertion Sort | Shell Sort |
| ---------------------- | -------------- | -------------- | ---------- |
| **시간 복잡도 (평균)** | O(n²)          | O(n²)          | O(n^1.5)   |
| **시간 복잡도 (최선)** | O(n²)          | O(n)           | O(n log n) |
| **시간 복잡도 (최악)** | O(n²)          | O(n²)          | O(n²)      |
| **공간 복잡도**        | O(1)           | O(1)           | O(1)       |
| **안정성**             | 불안정         | 안정           | 불안정     |
| **적응형**             | 아니오         | 예             | 부분적     |

## 🎨 애니메이션 특징

### 색상 코딩

- **노란색 (#FFD93D)**: 현재 처리 중인 요소
- **빨간색 (#FF6B6B)**: Selection Sort / 비교 대상
- **청록색 (#4ECDC4)**: Insertion Sort / 삽입 위치
- **파란색 (#45B7D1)**: Shell Sort / gap 그룹

### 시각적 요소

- 실시간 단계별 진행 상황
- 각 알고리즘의 고유한 동작 방식 표시
- 성능 지표와 설명 텍스트
- 깔끔하고 직관적인 UI

## 📈 성능 분석

### 작은 데이터셋 (n ≤ 50)

1. **Insertion Sort** - 가장 빠름
2. **Shell Sort** - 중간 성능
3. **Selection Sort** - 가장 느림

### 중간 크기 데이터셋 (50 < n ≤ 1000)

1. **Shell Sort** - 가장 빠름
2. **Insertion Sort** - 중간 성능
3. **Selection Sort** - 가장 느림

## 🔧 의존성

- Python 3.7+
- matplotlib
- numpy
- pillow (애니메이션 저장용)

## 📝 사용 사례

### 교육 목적

- 알고리즘 학습 및 이해
- 정렬 과정의 시각적 비교
- 성능 특성 분석

### 연구 목적

- 알고리즘 성능 측정
- 데이터 특성에 따른 성능 변화 분석
- 최적화 기법 연구

### 개발 목적

- 적절한 정렬 알고리즘 선택 가이드
- 성능 요구사항 분석
- 코드 최적화 참고

## 🤝 기여

이 프로젝트는 교육 목적으로 제작되었으며, 다음과 같은 기여를 환영합니다:

- 버그 리포트
- 성능 개선 제안
- 새로운 시각화 기법
- 추가 알고리즘 비교

## 📄 라이선스

이 프로젝트는 교육 목적으로 제작되었으며, 자유롭게 사용하실 수 있습니다.

## 🙏 감사의 말

- matplotlib 팀: 시각화 라이브러리 제공
- Python 커뮤니티: 훌륭한 프로그래밍 언어 제공
- 알고리즘 연구자들: 이론적 배경 제공
