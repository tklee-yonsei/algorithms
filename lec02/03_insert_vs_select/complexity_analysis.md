# Insertion Sort vs Selection Sort - 복잡도 분석

## 시간 복잡도 (Time Complexity) 비교

### Big O Notation 분석

| 정렬 알고리즘      | Best Case | Average Case | Worst Case |
| ------------------ | --------- | ------------ | ---------- |
| **Selection Sort** | O(n²)     | O(n²)        | O(n²)      |
| **Insertion Sort** | O(n)      | O(n²)        | O(n²)      |

### 상세 분석

#### Selection Sort

- **Best Case**: O(n²) - 이미 정렬되어 있어도 모든 요소를 비교해야 함
- **Average Case**: O(n²) - 평균적으로 n²/2 비교와 n 교환
- **Worst Case**: O(n²) - 역순으로 정렬되어 있어도 동일한 복잡도

**이유**: Selection Sort는 항상 전체 배열을 스캔하여 최솟값을 찾아야 하므로, 데이터의 상태와 관계없이 일정한 복잡도를 가집니다.

#### Insertion Sort

- **Best Case**: O(n) - 이미 정렬된 배열의 경우
- **Average Case**: O(n²) - 평균적으로 n²/4 비교와 n²/4 교환
- **Worst Case**: O(n²) - 역순으로 정렬된 배열의 경우

**이유**: Insertion Sort는 적응형 알고리즘으로, 이미 정렬된 부분이 많을수록 효율적입니다.

## 공간 복잡도 (Space Complexity)

| 정렬 알고리즘      | 공간 복잡도 | 설명                           |
| ------------------ | ----------- | ------------------------------ |
| **Selection Sort** | O(1)        | 제자리 정렬 (In-place sorting) |
| **Insertion Sort** | O(1)        | 제자리 정렬 (In-place sorting) |

### 상세 설명

#### Selection Sort 공간 복잡도

- **추가 메모리**: O(1)
- **사용하는 변수들**:
  - `minIndex`: 최솟값의 인덱스 저장
  - `temp`: 교환을 위한 임시 변수
- **특징**: 입력 배열 외에 상수 개의 변수만 사용

#### Insertion Sort 공간 복잡도

- **추가 메모리**: O(1)
- **사용하는 변수들**:
  - `key`: 현재 삽입할 요소
  - `j`: 비교할 인덱스
- **특징**: 입력 배열 외에 상수 개의 변수만 사용

## 실제 성능 비교

### 시나리오별 성능

1. **이미 정렬된 배열**

   - Selection Sort: O(n²) - 비효율적
   - Insertion Sort: O(n) - 매우 효율적

2. **역순으로 정렬된 배열**

   - Selection Sort: O(n²) - 일정한 성능
   - Insertion Sort: O(n²) - 최악의 경우

3. **랜덤 배열**

   - Selection Sort: O(n²) - 일정한 성능
   - Insertion Sort: O(n²) - 평균적인 성능

4. **거의 정렬된 배열**
   - Selection Sort: O(n²) - 비효율적
   - Insertion Sort: O(n) - 매우 효율적

## 안정성 (Stability)

| 정렬 알고리즘      | 안정성            |
| ------------------ | ----------------- |
| **Selection Sort** | 불안정 (Unstable) |
| **Insertion Sort** | 안정 (Stable)     |

### 안정성 설명

- **Selection Sort**: 동일한 값의 상대적 순서가 변경될 수 있음
- **Insertion Sort**: 동일한 값의 상대적 순서가 유지됨

## 사용 권장 사항

### Selection Sort 사용 시기

- 작은 데이터셋 (n < 50)
- 교환 횟수를 최소화해야 하는 경우
- 메모리 사용량이 매우 제한적인 경우

### Insertion Sort 사용 시기

- 작은 데이터셋 (n < 50)
- 이미 거의 정렬된 데이터
- 안정성이 중요한 경우
- 온라인 정렬 (데이터가 실시간으로 들어오는 경우)

## 결론

- **작은 데이터셋**: 두 알고리즘 모두 적합
- **거의 정렬된 데이터**: Insertion Sort가 훨씬 우수
- **안정성 필요**: Insertion Sort 선택
- **교환 횟수 최소화**: Selection Sort 선택
- **대용량 데이터**: 둘 다 비효율적 (더 나은 알고리즘 사용 권장)
