FROM ubuntu:22.04

# 환경 변수 설정
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# 시스템 패키지 업데이트 및 기본 도구 설치
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    git \
    vim \
    nano \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# C/C++ 개발 도구 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    make \
    cmake \
    clang \
    clang-format \
    valgrind \
    gdb \
    && rm -rf /var/lib/apt/lists/*

# Clangd 설치
RUN apt-get update && apt-get install -y \
    clangd \
    && rm -rf /var/lib/apt/lists/*

# Python 설치
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Python 패키지 설치
RUN pip3 install --no-cache-dir \
    autopep8 \
    black \
    flake8 \
    pytest \
    numpy \
    matplotlib

# 작업 디렉토리 설정
WORKDIR /workspace

# 사용자 생성
RUN useradd -m -s /bin/bash vscode && \
    echo "vscode ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# 소유권 변경
RUN chown -R vscode:vscode /workspace

USER vscode

# 기본 명령어
CMD ["/bin/bash"]
