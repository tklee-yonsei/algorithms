# 랜덤 프로그램 (Random Programs)

이 디렉토리에는 Python과 C로 작성된 간단한 랜덤 프로그램들이 포함되어 있습니다.

## 파일 구성

- `random_program.py` - Python으로 작성된 랜덤 프로그램
- `random_program.c` - C로 작성된 랜덤 프로그램
- `random_program` - 컴파일된 C 실행 파일

## 기능

두 프로그램 모두 다음과 같은 기능을 제공합니다:

1. **기본 랜덤 숫자 생성**: 시드 없이 랜덤 숫자 생성
2. **시드 기반 랜덤 숫자 생성**: 고정된 시드를 사용하여 재현 가능한 랜덤 숫자 생성
3. **시간 기반 시드**: 현재 시간을 시드로 사용
4. **랜덤 선택**: 리스트에서 랜덤 요소 선택

## 실행 방법

### Python 프로그램

```bash
python3 random_program.py
```

### C 프로그램

```bash
# 컴파일 (이미 컴파일되어 있음)
gcc -o random_program random_program.c

# 실행
./random_program
```

## 주요 개념

### 시드(Seed)란?

- 랜덤 숫자 생성기의 초기값
- 같은 시드를 사용하면 항상 같은 순서의 랜덤 숫자가 생성됨
- 디버깅이나 재현 가능한 결과가 필요할 때 유용

### Python vs C 랜덤 함수

- **Python**: `random` 모듈 사용 (`random.randint()`, `random.seed()` 등)
- **C**: `stdlib.h`의 `rand()`, `srand()` 함수 사용

### 랜덤 범위 설정

- **Python**: `random.randint(a, b)` - a부터 b까지 (포함)
- **C**: `(rand() % range) + min` - min부터 min+range-1까지
