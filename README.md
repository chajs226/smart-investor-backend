# Smart Investor Backend

AI 기반 주식 투자 분석 서비스 백엔드 API

## 🚀 Features

- **재무 데이터 크롤링**: 네이버 금융에서 기업 재무제표 수집
- **AI 분석**: Perplexity AI를 활용한 투자 분석 리포트 생성
- **데이터 저장**: Supabase를 통한 분석 결과 저장 및 관리
- **RESTful API**: FastAPI 기반의 빠르고 안정적인 API

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **AI**: Perplexity AI API
- **Database**: Supabase (PostgreSQL)
- **Web Scraping**: BeautifulSoup4, Requests
- **Data Processing**: Pandas
- **Deployment**: Render

## 📋 Prerequisites

- Python 3.10 이상
- Perplexity API Key
- Supabase Account

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/chajs226/smart-investor-backend.git
cd smart-investor-backend
```

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Variables

`.env.example` 파일을 복사하여 `.env` 파일 생성:

```bash
cp .env.example .env
```

`.env` 파일 수정:

```bash
# Supabase Configuration
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key

# Perplexity API Configuration
PERPLEXITY_API_KEY=pplx-your-api-key
PERPLEXITY_DEFAULT_MODEL=sonar

# Server Configuration
ENABLE_SERVER_SAVE=true
```

**환경 변수 발급 방법**:
- **Perplexity API Key**: [Perplexity Settings](https://www.perplexity.ai/settings/api)
- **Supabase Keys**: [Supabase Dashboard](https://supabase.com/dashboard) → Project Settings → API

## 🚀 Running Locally

### Development Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

또는 start 스크립트 사용:

```bash
./start.sh
```

서버 실행 후 다음 URL에서 확인:
- API: http://localhost:8000
- API 문서: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc

## 📁 Project Structure

```
smart-investor-backend/
├── app/
│   ├── main.py              # FastAPI 앱 초기화 및 설정
│   ├── api/                 # API 엔드포인트
│   │   ├── analysis.py      # 투자 분석 API
│   │   └── financial.py     # 재무 데이터 API
│   ├── models/              # 데이터 모델
│   │   ├── analysis.py      
│   │   └── financial.py     
│   └── services/            # 비즈니스 로직
│       ├── naver_crawler.py      # 네이버 금융 크롤러
│       ├── perplexity_service.py # Perplexity AI 서비스
│       └── supabase_service.py   # Supabase 연동
├── docs/                    # 문서
├── tests/                   # 테스트
├── temp/                    # 임시 파일
├── requirements.txt         # Python 의존성
├── .env.example            # 환경 변수 예시
└── start.sh                # 서버 시작 스크립트
```

## 🔒 Security

### 환경 변수 관리

- **로컬 개발**: `.env` 파일 사용 (Git에 커밋되지 않음)
- **프로덕션**: Render의 Environment Variables 기능 사용

**⚠️ 중요**: `.env` 파일은 절대 Git에 커밋하지 마세요!

`.gitignore`에 이미 포함되어 있습니다:
```gitignore
.env*
!.env.example
```

## 🌐 Deployment (Render)

### 빠른 배포 가이드

1. [Render Dashboard](https://dashboard.render.com) 접속
2. **"New +"** → **"Web Service"** 선택
3. GitHub 저장소 연결
4. **Environment** 탭에서 환경 변수 설정
5. **"Create Web Service"** 클릭

### 환경 변수 설정

Render Dashboard → Your Service → Environment → Add Environment Variable

필수 환경 변수:
- `SUPABASE_URL`
- `SUPABASE_SERVICE_ROLE_KEY`
- `PERPLEXITY_API_KEY`
- `PERPLEXITY_DEFAULT_MODEL`
- `ENABLE_SERVER_SAVE`

**자세한 배포 가이드**: [`docs/RENDER_DEPLOYMENT_GUIDE.md`](./docs/RENDER_DEPLOYMENT_GUIDE.md)

**빠른 시작**: [`docs/QUICK_START_RENDER.md`](./docs/QUICK_START_RENDER.md)

## 📚 API Documentation

### API 엔드포인트

#### 1. 재무 데이터 수집
```http
GET /api/financial/{stock_code}
```

**Parameters**:
- `stock_code`: 주식 코드 (예: 005930)

**Response**:
```json
{
  "stock_code": "005930",
  "company_name": "삼성전자",
  "financials": [...]
}
```

#### 2. AI 투자 분석
```http
POST /api/analysis
```

**Request Body**:
```json
{
  "stock_code": "005930",
  "company_name": "삼성전자",
  "market": "KOSPI"
}
```

**Response**:
```json
{
  "analysis_id": "uuid",
  "report": "AI 생성 분석 리포트...",
  "created_at": "2025-12-07T..."
}
```

### 자세한 API 문서

서버 실행 후 다음 URL에서 대화형 API 문서 확인:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🧪 Testing

### Run Tests

```bash
pytest
```

### Run with Coverage

```bash
pytest --cov=app tests/
```

### Test Specific Module

```bash
pytest tests/test_naver_crawler.py
```

## 🐛 Troubleshooting

### 환경 변수를 찾을 수 없음

```bash
# 서버 시작 로그 확인
❌ Missing required environment variable: PERPLEXITY_API_KEY
```

**해결 방법**:
1. `.env` 파일이 프로젝트 루트에 있는지 확인
2. 환경 변수명의 오타 확인
3. `.env.example`과 비교하여 누락된 변수 확인

### API 요청 실패

```bash
# 401 Unauthorized
```

**해결 방법**:
1. API 키가 유효한지 확인
2. Perplexity/Supabase 대시보드에서 키 상태 확인
3. 키를 재생성하고 `.env` 파일 업데이트

### 크롤링 실패

```bash
# 네이버 금융 데이터를 가져올 수 없음
```

**해결 방법**:
1. 네트워크 연결 확인
2. 주식 코드가 올바른지 확인
3. 네이버 금융 사이트 구조 변경 여부 확인

## 📝 Development

### Code Style

```bash
# Format code
black app/

# Lint
flake8 app/

# Type check
mypy app/
```

### Git Workflow

```bash
# Feature branch
git checkout -b feature/your-feature

# Commit
git commit -m "feat: add new feature"

# Push
git push origin feature/your-feature
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is private and proprietary.

## 👥 Authors

- **chajs226** - Initial work

## 🔗 Related Projects

- [Smart Investor Frontend](https://github.com/chajs226/smart-investor-frontend) - Next.js 기반 프론트엔드

## 📞 Support

문제가 발생하면 다음을 확인하세요:
1. [Issues](https://github.com/chajs226/smart-investor-backend/issues)
2. [Documentation](./docs/)
3. Render 로그: Dashboard → Your Service → Logs

---

**Last Updated**: 2025년 12월 7일
