"""로깅 설정 모듈.

이 모듈은 한국어 프롬프트 엔지니어링 시스템의 로깅 구성을 제공합니다.
콘솔과 파일 모두에 로그를 출력하며, ComfyUI 환경에서도 정상 작동합니다.
"""

import logging
import os
from typing import Optional

# 로그 포맷 정의
LOG_FORMAT = '[%(asctime)s] [%(levelname)s] [%(name)s:%(lineno)d] - %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

# 로거 캐시 (성능 최적화)
_logger_cache = {}


def setup_console_handler() -> logging.Handler:
    """콘솔 핸들러 설정.
    
    ComfyUI 터미널에서 로그를 보여주기 위해 항상 활성화됩니다.
    
    반환값:
        콘솔 로그 핸들러
    """
    console_handler = logging.StreamHandler()
    console_formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)
    console_handler.setFormatter(console_formatter)
    return console_handler


def setup_file_handler() -> Optional[logging.Handler]:
    """파일 핸들러 설정 (선택적).
    
    로그를 파일에 저장합니다.
    
    반환값:
        파일 로그 핸들러 또는 None (파일 생성 실패 시)
    """
    try:
        # 프로젝트 루트에 로그 파일 생성
        log_file = 'korean_prompt_engineer.log'
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_formatter = logging.Formatter(LOG_FORMAT, datefmt=DATE_FORMAT)
        file_handler.setFormatter(file_formatter)
        return file_handler
    except Exception as e:
        # 파일 핸들러 설정 실패 시 로그 출력
        print(f"파일 로그 핸들러 설정 실패: {e}")
        return None


def get_logger(name: str) -> logging.Logger:
    """로거를 생성하거나 반환합니다.
    
    로거 캐시를 사용하여 성능을 최적화하고,
    필요시 로거를 새로 생성합니다.
    
    인자:
        name: 로거 이름
        
    반환값:
        설정된 로거 인스턴스
    """
    # 캐시에 로거가 이미 존재하는지 확인
    if name in _logger_cache:
        return _logger_cache[name]
    
    try:
        # 로거 생성
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        
        # 이미 핸들러가 존재하지 않으면 추가
        if not logger.handlers:
            # 콘솔 핸들러 추가
            console_handler = setup_console_handler()
            logger.addHandler(console_handler)
            
            # 파일 핸들러 추가 (선택적)
            file_handler = setup_file_handler()
            if file_handler:
                logger.addHandler(file_handler)
        
        # 캐시에 저장
        _logger_cache[name] = logger
        return logger
        
    except Exception as e:
        # 로거 설정 실패 시 기본 로거 반환
        print(f"로거 설정 실패: {e}")
        return logging.getLogger('default')


# 메인 로거 생성 (모듈 레벨 로거)
logger = get_logger(__name__)
