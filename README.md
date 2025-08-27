# Algorithms Study

알고리즘 학습을 위한 개발 환경입니다.

## 개발 환경

### VSCode Dev Container 사용 (추천)

1. VSCode에서 `Dev Containers` 확장 설치
2. `Ctrl+Shift+P` (또는 `Cmd+Shift+P`) → `Dev Containers: Reopen in Container`
3. 컨테이너 빌드 및 설정 자동 완료

### Docker Compose 사용

```bash
# 컨테이너 빌드 및 실행
docker-compose up -d

# 컨테이너에 접속
docker-compose exec algorithms-dev bash

# 컨테이너 중지
docker-compose down
```

### 직접 Docker 사용

```bash
# 이미지 빌드
docker build -t algorithms-dev .

# 컨테이너 실행
docker run -it --rm -v $(pwd):/workspace algorithms-dev
```

## 포함된 도구

### C/C++ 개발

- GCC, Clang 컴파일러
- Make, CMake 빌드 도구
- Clang-format 포매터
- GDB 디버거
- Valgrind 메모리 검사 도구

### Python 개발

- Python 3.11
- autopep8, black 포매터
- flake8 린터
- pytest 테스트 프레임워크
- numpy, matplotlib 라이브러리

## 프로젝트 구조

```
algorithms/
├── lec1/                  # 강의 1
├── lec.../                # 강의 ...
├── .devcontainer/         # VSCode 개발 컨테이너 설정
├── .vscode/               # VSCode 설정
├── setup.cfg              # Python 포매터 설정
├── .clang-format          # C/C++ 포매터 설정
├── Dockerfile             # Docker 이미지 정의
└── docker-compose.yml     # Docker Compose 설정
```

## 사용법

### C언어 컴파일 및 실행

```bash
cd lec1
gcc -o multiplyByTwo.o multiplyByTwo.c
./multiplyByTwo.o
```

### Python 실행

```bash
cd lec1
python3 multiplyByTwo.py
```

### 코드 포매팅

- C/C++: `clang-format -i *.c *.h`
- Python: `autopep8 --in-place --indent-size=2 *.py`
