# regex.py - 시작 코드
from typing import Optional, Tuple

class RegexMatcher:
    """
    정규식 매칭 알고리즘 구현 - 시작 코드
    
    지원하는 메타 문자:
    - '.' : 임의의 한 문자와 매칭
    - '*' : 바로 앞 문자의 0개 이상 반복
    - '^' : 문자열의 시작 (선택사항)
    - '$' : 문자열의 끝 (선택사항)
    
    시간 복잡도: O(m * n) where m is pattern length, n is text length
    공간 복잡도: O(1) (재귀 스택 제외)
    """
    
    def __init__(self):
        pass
    
    def match(self, pattern: str, text: str) -> bool:
        """
        기본 정규식 매칭 함수
        
        Args:
            pattern (str): 정규식 패턴
            text (str): 검색할 텍스트
            
        Returns:
            bool: 매칭되면 True, 아니면 False
        """
        # TODO: 기본 정규식 매칭 구현
        # 1. 베이스 케이스: 패턴이 끝나면 성공
        # 2. 다음 문자가 '*'인 경우 (x* 패턴) -> match_star 호출
        # 3. 텍스트가 끝났는데 패턴이 남아있으면 실패
        # 4. 현재 문자가 일치하거나 '.'인 경우 -> 재귀 호출
        # 5. 매칭 실패
        
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
        # TODO: '*' 메타문자 처리
        # 1. 0개 매칭 시도 (c*를 빈 문자열로 매칭)
        # 2. 1개 이상 매칭 시도 (반복)
        #    - 현재 텍스트 문자가 c와 일치하거나 c가 '.'인 경우
        #    - 텍스트를 한 문자씩 진행하면서 재귀 호출
        
        return False
    
    def match_anywhere(self, pattern: str, text: str) -> bool:
        """
        텍스트의 어느 위치에서든 패턴 매칭 시도
        
        Args:
            pattern (str): 정규식 패턴
            text (str): 검색할 텍스트
            
        Returns:
            bool: 매칭되면 True, 아니면 False
        """
        # TODO: 텍스트의 어느 위치에서든 매칭 시도
        # 1. 빈 패턴은 항상 매칭
        # 2. '^'로 시작하는 패턴은 텍스트 시작에서만 매칭 (선택사항)
        # 3. '$'로 끝나는 패턴은 텍스트 끝에서만 매칭 (선택사항)
        # 4. 텍스트의 각 위치에서 match 함수 호출
        
        return False
    
    def validate_pattern(self, pattern: str) -> bool:
        """
        패턴의 문법 오류 검사
        
        Args:
            pattern (str): 검사할 패턴
            
        Returns:
            bool: 유효하면 True, 아니면 False
        """
        # TODO: 패턴 유효성 검사
        # 1. 빈 패턴 체크
        # 2. '*'가 맨 앞에 오면 안됨
        # 3. '**' 패턴은 유효하지 않음
        
        return True
    
    def find_match(self, pattern: str, text: str) -> Optional[Tuple[int, int]]:
        """
        매칭되는 첫 번째 위치와 길이 반환 (선택사항)
        
        Args:
            pattern (str): 정규식 패턴
            text (str): 검색할 텍스트
            
        Returns:
            Optional[Tuple[int, int]]: (시작 위치, 길이) 또는 None
        """
        # TODO: 매칭되는 첫 번째 위치 찾기 (선택사항)
        return None
    
    def replace_first(self, pattern: str, text: str, replacement: str) -> str:
        """
        첫 번째 매칭되는 부분을 replacement로 교체 (선택사항)
        
        Args:
            pattern (str): 정규식 패턴
            text (str): 원본 텍스트
            replacement (str): 교체할 문자열
            
        Returns:
            str: 교체된 텍스트
        """
        # TODO: 첫 번째 매칭 부분 교체 (선택사항)
        return text


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
    ]
    
    print("=== 기본 매칭 테스트 ===")
    pass_count = 0
    
    for pattern, text, expected, description in test_cases:
        result = matcher.match_anywhere(pattern, text)
        passed = (result == expected)
        status = "PASS" if passed else "FAIL"
        
        print(f"패턴: '{pattern:<8}', 텍스트: '{text:<10}' -> {str(result):<5} ({status}) [{description}]")
        
        if passed:
            pass_count += 1
    
    print(f"\n테스트 결과: {pass_count}/{len(test_cases)} 통과\n")
    
    # 패턴 검증 테스트
    print("=== 패턴 검증 테스트 ===")
    test_patterns = ["*abc", "a**", "", "abc", "a*b*c"]
    
    for test_pattern in test_patterns:
        is_valid = matcher.validate_pattern(test_pattern)
        print(f"패턴: '{test_pattern:<5}' -> {'유효' if is_valid else '무효'}")
    print()
    
    print("테스트 완료")


if __name__ == "__main__":
    run_tests()