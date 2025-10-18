import os
from typing import Any, Dict, Optional

try:
    from supabase import create_client, Client
except Exception:  # pragma: no cover - package may not be installed locally yet
    create_client = None  # type: ignore
    Client = Any  # type: ignore


class SupabaseReportStore:
    _client: Optional[Client] = None

    @classmethod
    def _get_client(cls) -> Client:
        if cls._client is not None:
            return cls._client
        url = os.getenv("SUPABASE_URL") or os.getenv("NEXT_PUBLIC_SUPABASE_URL")
        key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
        if not url or not key:
            raise RuntimeError("Supabase configuration missing: SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY are required")
        if create_client is None:
            raise RuntimeError("supabase package not installed. Add 'supabase' to requirements.txt")
        cls._client = create_client(url, key)
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
        client = cls._get_client()
        payload: Dict[str, Any] = {
            "market": market,
            "symbol": symbol,
            "name": name,
            "sector": sector,
            "report": report,
        }
        if user_id:
            payload["user_id"] = user_id
        resp = client.table("reports").insert(payload).execute()
        # Basic error surface
        if getattr(resp, "error", None):
            raise RuntimeError(str(resp.error))


