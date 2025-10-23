import os
from typing import Any, Dict, Optional
import logging

try:
    from supabase import create_client, Client
except Exception:  # pragma: no cover - package may not be installed locally yet
    create_client = None  # type: ignore
    Client = Any  # type: ignore

logger = logging.getLogger(__name__)


class SupabaseReportStore:
    _client: Optional[Client] = None

    @classmethod
    def _get_client(cls) -> Client:
        if cls._client is not None:
            return cls._client
        url = os.getenv("SUPABASE_URL") or os.getenv("NEXT_PUBLIC_SUPABASE_URL")
        key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
        
        # 디버그 로그 추가
        logger.info(f"[Supabase] Attempting to connect...")
        logger.info(f"[Supabase] URL found: {bool(url)}")
        logger.info(f"[Supabase] KEY found: {bool(key)}")
        
        if not url or not key:
            raise RuntimeError("Supabase configuration missing: SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY are required")
        if create_client is None:
            raise RuntimeError("supabase package not installed. Add 'supabase' to requirements.txt")
        cls._client = create_client(url, key)
        logger.info(f"[Supabase] Client created successfully")
        return cls._client

    @classmethod
    def save_report(
        cls,
        *,
        market: str,
        symbol: str,
        name: str,
        sector: Optional[str],
        report: Dict[str, Any],
        user_id: Optional[str] = None,
    ) -> None:
        """
        stock_analyses 테이블에 분석 결과 저장
        
        스키마:
        - market: 'KOSPI' | 'KOSDAQ' | 'NASDAQ'
        - symbol: 종목코드
        - name: 회사명
        - sector: 섹터 (nullable)
        - report: 분석 내용 (텍스트)
        - financial_table: 재무 테이블 (텍스트, nullable)
        - compare_periods: 비교 기간 배열 (nullable)
        - model: 사용 모델 (nullable)
        - citations: 인용 출처 배열 (nullable)
        - created_at, updated_at: 타임스탬프 (자동)
        """
        from datetime import datetime
        
        client = cls._get_client()
        
        # report dict를 필드별로 분해
        payload: Dict[str, Any] = {
            "market": market,
            "symbol": symbol,
            "name": name,
            "sector": sector,
            "report": report.get("analysis", ""),  # 분석 내용 (텍스트)
            "financial_table": report.get("financial_table"),
            "compare_periods": report.get("compare_periods"),
            "model": report.get("model"),
            "citations": report.get("citations"),
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat(),
        }
        
        # 디버그: 저장할 payload 로깅
        logger.info(f"[Supabase] Saving payload:")
        logger.info(f"  - market: {payload['market']}")
        logger.info(f"  - symbol: {payload['symbol']}")
        logger.info(f"  - compare_periods: {payload['compare_periods']}")
        logger.info(f"  - model: {payload['model']}")
        
        # user_id는 stock_analyses 테이블에 없으므로 제거
        
        resp = client.table("stock_analyses").insert(payload).execute()
        # Basic error surface
        if getattr(resp, "error", None):
            raise RuntimeError(str(resp.error))
        
        logger.info(f"[Supabase] Analysis saved successfully: {symbol} ({name})")


