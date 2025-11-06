"""응답 캐싱 관리 모듈.

이 모듈은 LLM 응답 및 프롬프트 확장 결과를 캐시하여
반복적인 API 호출을 줄이고 성능을 향상시킵니다.
캐시는 diskcache 라이브러리를 사용하여 구현됩니다.
"""

import os
import json
from typing import Any, Optional
from diskcache import Cache
from .logger import get_logger

logger = get_logger(__name__)


class CacheManager:
    """응답 캐싱 관리."""

    def __init__(self, cache_dir: str = "~/.korean_prompt_engineer/cache"):
        """캐시 초기화.

        Args:
            cache_dir: 캐시 저장 디렉토리 경로
        """
        # ~를 실제 홈 디렉토리로 확장
        expanded_cache_dir = os.path.expanduser(cache_dir)
        
        # 캐시 디렉토리 생성
        os.makedirs(expanded_cache_dir, exist_ok=True)
        
        # diskcache 인스턴스 생성
        self.cache = Cache(expanded_cache_dir)
        logger.debug(f"캐시 관리자 초기화 완료: {expanded_cache_dir}")

    def get(self, key: str) -> Optional[Any]:
        """캐시에서 데이터 조회.

        Args:
            key: 캐시 키

        Returns:
            캐시된 데이터 또는 None
        """
        try:
            cached_data = self.cache.get(key)
            if cached_data is not None:
                logger.debug(f"캐시 히트: {key}")
            else:
                logger.debug(f"캐시 미스: {key}")
            return cached_data
        except Exception as e:
            logger.warning(f"캐시 조회 실패: {key}, 오류: {e}")
            return None

    def set(self, key: str, value: Any, ttl_days: int = 7):
        """캐시에 데이터 저장.

        Args:
            key: 캐시 키
            value: 저장할 값
            ttl_days: TTL (일 단위), 기본값 7일
        """
        try:
            # TTL을 초 단위로 변환 (기본 7일 = 604800초)
            ttl_seconds = ttl_days * 24 * 60 * 60
            
            # 데이터를 JSON으로 직렬화하여 저장
            serialized_value = json.dumps(value)
            self.cache.set(key, serialized_value, expire=ttl_seconds)
            logger.debug(f"캐시 저장 완료: {key}, TTL: {ttl_days}일")
        except Exception as e:
            logger.error(f"캐시 저장 실패: {key}, 오류: {e}")

    def clear(self):
        """캐시 전체 삭제."""
        try:
            self.cache.clear()
            logger.info("캐시 전체 삭제 완료")
        except Exception as e:
            logger.error(f"캐시 삭제 실패: {e}")

    def get_stats(self) -> dict:
        """캐시 통계 (크기, 항목 수) 반환.

        Returns:
            캐시 통계 딕셔너리
        """
        try:
            stats = self.cache.stats()
            return {
                "size": stats[0],
                "hits": stats[1],
                "misses": stats[2],
                "items": len(self.cache)
            }
        except Exception as e:
            logger.error(f"캐시 통계 조회 실패: {e}")
            return {}
