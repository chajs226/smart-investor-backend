#!/bin/bash
# 백엔드 서버 시작 스크립트 (타임아웃 설정 포함)

export ENABLE_SERVER_SAVE=true

# 가상환경이 있다면 활성화
if [ -d "venv" ]; then
    source venv/bin/activate
elif [ -d ".venv" ]; then
    source .venv/bin/activate
else
    echo "가상환경을 찾을 수 없습니다. 새로 생성합니다..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
fi

# Uvicorn 옵션:
# --timeout-keep-alive: 유휴 연결 타임아웃 (초)
# --timeout-graceful-shutdown: 종료 대기 시간
# --reload: 코드 변경 시 자동 재시작 (개발용)
uvicorn app.main:app \
  --host 0.0.0.0 \
  --port 8000 \
  --timeout-keep-alive 350 \
  --timeout-graceful-shutdown 30 \
  --reload
