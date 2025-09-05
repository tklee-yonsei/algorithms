# regex.py
import time
from dataclasses import dataclass
from typing import Optional, List, Tuple

@dataclass
class MatchStats:
    """매칭 통계 정보를 저장하는 클래스"""
    result: bool
    comparisons: int
    recursion_depth: int
    execution_time: float  # milliseconds

class RegexMatcher:
    """
    정규식 매칭 알고리즘 구현
    
    지원하는 메타 문자:
    - '.' : 임의의 한 문자와 매칭
    - '*' : 바로 앞 문자의 0개 이상 반복
    - '^' : 문자열의 시작
    - '$' : 문자열의 끝
    
    시간 복잡도: O(m * n) where m is pattern length, n is text length
    공간 복잡도: O(1) (재귀 스택 제외)
    """
    
    def __init__(self):
        # 통계용 변수들
        self.comparisons = 0
        self.max_recursion = 0
        self.current_recursion = 0
    
    def match(self, pattern: str, text: str) -> bool:
        """
        기본 정규식 매칭 함수
        
        Args:
            pattern (str): 정규식 패턴
            text (str): 검색할 텍스트
            
        Returns:
            bool: 매칭되면 True, 아니면 False
        """
        self.comparisons += 1
        self.current_recursion += 1
        if self.current_recursion > self.max_recursion:
            self.max_recursion = self.current_recursion
        
        # 베이스 케이스: 패턴이 끝나면 성공
        if not pattern:
            self.current_recursion -= 1
            return True
        
        # 다음 문자가 '*'인 경우 (x* 패턴)
        if len(pattern) >= 2 and pattern[1] == '*':
            result = self.match_star(pattern[0], pattern[2:], text)
            self.current_recursion -= 1
            return result
        
        # 텍스트가 끝났는데 패턴이 남아있으면 실패
        if not text:
            self.current_recursion -= 1
            return False
        
        # 현재 문자가 일치하거나 '.'인 경우
        if pattern[0] == text[0] or pattern[0] == '.':
            result = self.match(pattern[1:], text[1:])
            self.current_recursion -= 1
            return result
        
        # 매칭 실패
        self.current_recursion -= 1
        return False
    
    def match_star(self, c: str, pattern: str, text: str) -> bool:
        """
        '*' 메타문자 처리 함수
        
        Args:
            c (str): '*' 앞의 문자 (또는 '.')
            pattern (str): '*' 이후의 패턴
            text (str): 검색할 텍스트
            
        Returns:
            bool: 매칭되면 True, 아니면 False
        """
        self.current_recursion += 1
        if self.current_recursion > self.max_recursion:
            self.max_recursion = self.current_recursion
        
        # 0개 매칭 시도 (c*를 빈 문자열로 매칭)
        if self.match(pattern, text):
            self.current_recursion -= 1
            return True
        
        # 1개 이상 매칭 시도
        i = 0
        while i < len(text) and (text[i] == c or c == '.'):
            i += 1
            if self.match(pattern, text[i:]):
                self.current_recursion -= 1
                return True
        
        # 모든 경우 실패
        self.current_recursion -= 1
        return False
    
    def match_here(self, pattern: str, text: str) -> bool:
        """
        텍스트의 시작 부분부터 매칭 시도
        
        Args:
            pattern (str): 정규식 패턴
            text (str): 검색할 텍스트
            
        Returns:
            bool: 매칭되면 True, 아니면 False
        """
        return self.match(pattern, text)
    
    def match_anywhere(self, pattern: str, text: str) -> bool:
        """
        텍스트의 어느 위치에서든 패턴 매칭 시도
        
        Args:
            pattern (str): 정규식 패턴
            text (str): 검색할 텍스트
            
        Returns:
            bool: 매칭되면 True, 아니면 False
        """
        # 빈 패턴은 항상 매칭
        if not pattern:
            return True
        
        # 패턴이 '^'로 시작하면 텍스트 시작에서만 매칭
        if pattern.startswith('^'):
            return self.match_here(pattern[1:], text)
        
        # 패턴이 '$'로 끝나면 텍스트 끝에서만 매칭
        if pattern.endswith('$'):
            temp_pattern = pattern[:-1]
            # 텍스트의 각 위치에서 시도하되, 끝까지 매칭되는지 확인
            for i in range(len(text) + 1):
                remaining_text = text[i:]
                if self.match(temp_pattern, remaining_text) and len(remaining_text) == len(temp_pattern):
                    return True
            return False
        
        # 텍스트의 각 위치에서 매칭 시도
        for i in range(len(text) + 1):
            if self.match_here(pattern, text[i:]):
                return True
        
        return False
    
    def validate_pattern(self, pattern: str) -> bool:
        """
        패턴의 문법 오류 검사
        
        Args:
            pattern (str): 검사할 패턴
            
        Returns:
            bool: 유효하면 True, 아니면 False
        """
        if not pattern:
            return True
        
        for i, char in enumerate(pattern):
            if char == '*':
                # '*'가 맨 앞에 올 수 없음
                if i == 0:
                    return False
                # '**' 패턴은 유효하지 않음
                if i > 0 and pattern[i-1] == '*':
                    return False
        
        return True
    
    def count_matches(self, pattern: str, text: str) -> int:
        """
        텍스트에서 패턴이 매칭되는 횟수 계산
        
        Args:
            pattern (str): 정규식 패턴
            text (str): 검색할 텍스트
            
        Returns:
            int: 매칭 횟수
        """
        count = 0
        for i in range(len(text) + 1):
            if self.match_here(pattern, text[i:]):
                count += 1
        return count
    
    def find_match(self, pattern: str, text: str) -> Optional[Tuple[int, int]]:
        """
        매칭되는 첫 번째 위치와 길이 반환
        
        Args:
            pattern (str): 정규식 패턴
            text (str): 검색할 텍스트
            
        Returns:
            Optional[Tuple[int, int]]: (시작 위치, 길이) 또는 None
        """
        for pos in range(len(text) + 1):
            for length in range(1, len(text) - pos + 2):
                if pos + length - 1 <= len(text):
                    substring = text[pos:pos + length]
                    if self.match(pattern, substring):
                        return (pos, length)
        return None
    
    def replace_first(self, pattern: str, text: str, replacement: str) -> str:
        """
        첫 번째 매칭되는 부분을 replacement로 교체
        
        Args:
            pattern (str): 정규식 패턴
            text (str): 원본 텍스트
            replacement (str): 교체할 문자열
            
        Returns:
            str: 교체된 텍스트
        """
        match_info = self.find_match(pattern, text)
        
        if match_info is None:
            return text  # 매칭되지 않음
        
        pos, length = match_info
        return text[:pos] + replacement + text[pos + length:]
    
    def replace_all(self, pattern: str, text: str, replacement: str) -> str:
        """
        모든 매칭되는 부분을 replacement로 교체
        
        Args:
            pattern (str): 정규식 패턴
            text (str): 원본 텍스트
            replacement (str): 교체할 문자열
            
        Returns:
            str: 교체된 텍스트
        """
        result = text
        
        while True:
            match_info = self.find_match(pattern, result)
            
            if match_info is None:
                break  # 더 이상 매칭되지 않음
            
            pos, length = match_info
            result = result[:pos] + replacement + result[pos + length:]
        
        return result
    
    def match_with_stats(self, pattern: str, text: str) -> MatchStats:
        """
        통계 정보와 함께 매칭 수행
        
        Args:
            pattern (str): 정규식 패턴
            text (str): 검색할 텍스트
            
        Returns:
            MatchStats: 매칭 결과와 통계 정보
        """
        # 통계 초기화
        self.comparisons = 0
        self.max_recursion = 0
        self.current_recursion = 0
        
        start_time = time.perf_counter()
        result = self.match_anywhere(pattern, text)
        end_time = time.perf_counter()
        
        execution_time = (end_time - start_time) * 1000  # ms
        
        return MatchStats(
            result=result,
            comparisons=self.comparisons,
            recursion_depth=self.max_recursion,
            execution_time=execution_time
        )


def run_tests():
    """테스트 케이스 실행"""
    print("=== 정규식 매칭 알고리즘 테스트 ===\n")
    
    matcher = RegexMatcher()
    
    # 기본 테스트 케이스들
    test_cases = [
        ("abc", "abc", True, "정확한 매칭"),
        ("a.c", "abc", True, "'.' 메타문자"),
        ("a.c", "adc", True, "'.' 메타문자 (다른 문자)"),
        ("a.c", "ac", False, "'.'는 반드시 한 문자 매칭"),
        ("a*", "", True, "'*' 0개 매칭"),
        ("a*", "a", True, "'*' 1개 매칭"),
        ("a*", "aaa", True, "'*' 여러 개 매칭"),
        ("a*b", "aaab", True, "'*' + 다른 문자"),
        (".*", "anything", True, "'.*'는 모든 문자열 매칭"),
        ("ca*t", "ct", True, "'a*' 0개 매칭"),
        ("ca*t", "cat", True, "'a*' 1개 매칭"),
        ("ca*t", "caaaat", True, "'a*' 여러 개 매칭"),
        ("ab*c", "ac", True, "b* 0개 매칭"),
        ("ab*c", "abc", True, "b* 1개 매칭"),
        ("ab*c", "abbbbc", True, "b* 여러 개 매칭"),
    ]
    
    print("=== 기본 매칭 테스트 ===")
    pass_count = 0
    
    for pattern, text, expected, description in test_cases:
        matcher = RegexMatcher()  # 새 인스턴스로 통계 리셋
        result = matcher.match_anywhere(pattern, text)
        passed = (result == expected)
        status = "PASS" if passed else "FAIL"
        
        print(f"패턴: '{pattern:<8}', 텍스트: '{text:<10}' -> {str(result):<5} ({status}) [{description}]")
        
        if passed:
            pass_count += 1
    
    print(f"\n테스트 결과: {pass_count}/{len(test_cases)} 통과\n")
    
    # 실제 사용 예시들
    print("=== 실제 사용 예시 ===")
    
    # 간단한 이메일 패턴
    emails = ["user@example.com", "test@test", "invalid-email", "a@b.c"]
    email_pattern = ".*@.*\\..*"  # 단순화된 이메일 패턴
    
    print(f"이메일 검증 (패턴: {email_pattern}):")
    matcher = RegexMatcher()
    for email in emails:
        is_valid = matcher.match_anywhere(email_pattern, email)
        print(f"  {email:<20} -> {'유효' if is_valid else '무효'}")
    print()
    
    # 문자열 치환 예시
    print("=== 문자열 치환 예시 ===")
    matcher = RegexMatcher()
    original_text = "Hello world, world is beautiful"
    pattern = "world"
    replacement = "universe"
    
    first_replaced = matcher.replace_first(pattern, original_text, replacement)
    all_replaced = matcher.replace_all(pattern, original_text, replacement)
    
    print(f"원본: {original_text}")
    print(f"첫 번째 치환: {first_replaced}")
    print(f"모든 치환: {all_replaced}")
    print()
    
    # 성능 테스트
    print("=== 성능 테스트 ===")
    long_text = "a" * 1000 + "b"
    complex_pattern = "a*b"
    
    matcher = RegexMatcher()
    stats = matcher.match_with_stats(complex_pattern, long_text)
    
    print(f"패턴: {complex_pattern}")
    print(f"텍스트 길이: {len(long_text)}")
    print(f"결과: {'매칭됨' if stats.result else '매칭되지 않음'}")
    print(f"실행 시간: {stats.execution_time:.3f} ms")
    print(f"비교 횟수: {stats.comparisons}")
    print(f"최대 재귀 깊이: {stats.recursion_depth}")
    print()
    
    # 패턴 검증 테스트
    print("=== 패턴 검증 테스트 ===")
    test_patterns = ["*abc", "a**", "", "abc", "a*b*c"]
    
    matcher = RegexMatcher()
    for test_pattern in test_patterns:
        is_valid = matcher.validate_pattern(test_pattern)
        print(f"패턴: '{test_pattern:<5}' -> {'유효' if is_valid else '무효'}")
    print()
    
    # 매칭 횟수 테스트
    print("=== 매칭 횟수 테스트 ===")
    count_text = "abcabcabc"
    count_pattern = "abc"
    
    matcher = RegexMatcher()
    match_count = matcher.count_matches(count_pattern, count_text)
    
    print(f"텍스트: {count_text}")
    print(f"패턴: {count_pattern}")
    print(f"매칭 횟수: {match_count}")
    print()
    
    # 고급 기능 데모
    print("=== 고급 기능 데모 ===")
    
    # 앵커 테스트 (^ 및 $)
    anchor_tests = [
        ("^hello", "hello world", True, "시작 앵커"),
        ("^hello", "say hello", False, "시작 앵커 실패"),
        ("world$", "hello world", True, "끝 앵커"),
        ("world$", "world peace", False, "끝 앵커 실패"),
    ]
    
    print("앵커 테스트:")
    for pattern, text, expected, description in anchor_tests:
        matcher = RegexMatcher()
        result = matcher.match_anywhere(pattern, text)
        status = "✓" if result == expected else "✗"
        print(f"  {status} 패턴: '{pattern}', 텍스트: '{text}' -> {result} [{description}]")
    print()
    
    print("테스트 완료")


def demo_practical_examples():
    """실용적인 예시 데모"""
    print("\n" + "="*50)
    print("=== 실용적인 정규식 예시 ===")
    
    matcher = RegexMatcher()
    
    # 로그 파싱 예시
    print("\n1. 로그 파싱:")
    log_entries = [
        "ERROR: File not found",
        "INFO: Server started",
        "ERROR: Database connection failed",
        "DEBUG: Processing request",
        "ERROR: Memory allocation failed"
    ]
    
    error_pattern = "ERROR.*"
    
    print(f"에러 로그 찾기 (패턴: {error_pattern}):")
    for log in log_entries:
        if matcher.match_anywhere(error_pattern, log):
            print(f"  ✓ {log}")
    
    # 간단한 URL 검증
    print("\n2. URL 검증:")
    urls = [
        "http://example.com",
        "https://www.google.com",
        "ftp://files.example.org",
        "invalid-url",
        "http://localhost"
    ]
    
    url_pattern = "http.*://.*"
    
    print(f"HTTP URL 찾기 (패턴: {url_pattern}):")
    for url in urls:
        matcher = RegexMatcher()
        if matcher.match_anywhere(url_pattern, url):
            print(f"  ✓ {url}")
    
    # 텍스트 정제
    print("\n3. 텍스트 정제:")
    messy_text = "Hello...world!!!How are you???"
    cleanup_patterns = [
        ("\\.\\.*", "."),  # 여러 점을 하나로
        ("!\\!*", "!"),   # 여러 느낌표를 하나로
        ("\\?\\?*", "?")  # 여러 물음표를 하나로
    ]
    
    print(f"원본: {messy_text}")
    cleaned = messy_text
    for pattern, replacement in cleanup_patterns:
        matcher = RegexMatcher()
        cleaned = matcher.replace_all(pattern, cleaned, replacement)
    print(f"정제 후: {cleaned}")


if __name__ == "__main__":
    run_tests()
    demo_practical_examples()