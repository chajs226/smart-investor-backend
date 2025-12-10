# Render 배포 - 환경 변수 설정 빠른 가이드

## 🚀 3단계로 끝내기

### 1️⃣ Render 대시보드 접속
- [Render Dashboard](https://dashboard.render.com) → 서비스 선택

### 2️⃣ Environment 탭으로 이동
- 왼쪽 메뉴에서 **"Environment"** 클릭

### 3️⃣ 환경 변수 추가
**"Add Environment Variable"** 또는 **"Add from .env"** 버튼 클릭

## 📋 필수 환경 변수 목록

```bash
# Supabase Configuration
SUPABASE_URL=https://mlbyllouvapjwfepgzeo.supabase.co
SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

# Perplexity API Configuration
PERPLEXITY_API_KEY=pplx-JxtIsxegxw0Qg3uyIi70...
PERPLEXITY_DEFAULT_MODEL=sonar

# Server Configuration
ENABLE_SERVER_SAVE=true
```

## 💡 환경 변수 값 찾기

### Perplexity API Key
1. [Perplexity AI Settings](https://www.perplexity.ai/settings/api) 접속
2. **"API Keys"** → **"Create API Key"** 클릭
3. 생성된 키 복사

### Supabase Keys
1. [Supabase Dashboard](https://supabase.com/dashboard) 접속
2. 프로젝트 선택
3. **"Project Settings"** → **"API"** 클릭
4. **URL**과 **service_role key** 복사

## ⚠️ 주의사항

- ✅ `.env` 파일은 **절대 Git에 커밋하지 마세요**
- ✅ 환경 변수 추가/수정 시 **자동으로 재배포**됩니다
- ✅ 로그에서 환경 변수가 제대로 로드되었는지 **확인하세요**

## 🔍 확인 방법

Render 로그에서 다음과 같은 메시지 확인:

```
✅ SUPABASE_URL: https://ml...****
✅ SUPABASE_SERVICE_ROLE_KEY: eyJhbGciOi...****
✅ PERPLEXITY_API_KEY: pplx-JxtIs...****
✅ All required environment variables are set!
```

## 📚 자세한 가이드

더 자세한 내용은 [`RENDER_DEPLOYMENT_GUIDE.md`](./RENDER_DEPLOYMENT_GUIDE.md) 참조

---

**문제 발생 시**: [Render 로그](https://dashboard.render.com) 확인 → Environment 탭 다시 확인 → Manual Deploy
