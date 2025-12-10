from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api import financial, analysis
import logging
import os
from dotenv import load_dotenv

# .env 파일 로드 (프로젝트 루트에서)
load_dotenv()

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# 필수 환경 변수 확인
REQUIRED_ENV_VARS = [
    "SUPABASE_URL",
    "SUPABASE_SERVICE_ROLE_KEY",
    "PERPLEXITY_API_KEY",
]

logger.info("🔍 Checking required environment variables...")
missing_vars = []
for var in REQUIRED_ENV_VARS:
    value = os.getenv(var)
    if not value:
        missing_vars.append(var)
        logger.error(f"❌ Missing required environment variable: {var}")
    else:
        # 키의 앞 10자와 뒤 4자만 표시 (보안)
        masked_value = f"{value[:10]}...{value[-4:]}" if len(value) > 14 else "****"
        logger.info(f"✅ {var}: {masked_value}")

if missing_vars:
    error_msg = f"Missing required environment variables: {', '.join(missing_vars)}"
    logger.error(f"❌ {error_msg}")
    raise ValueError(error_msg)

logger.info("✅ All required environment variables are set!")

app = FastAPI(
    title="Investor Routiner API",
    description="기업 재무분석 자동화 블로그 글 생성 서비스 API",
    version="1.0.0"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 프로덕션에서는 실제 프론트엔드 도메인으로 변경
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(financial.router, prefix="/api/financial", tags=["financial"])
app.include_router(analysis.router, prefix="/api/analysis", tags=["analysis"])

@app.get("/")
async def root():
    return {"message": "Investor Routiner API"}
