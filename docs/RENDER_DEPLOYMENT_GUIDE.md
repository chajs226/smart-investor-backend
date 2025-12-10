# Render 배포 가이드 - 환경 변수 설정

## 📋 개요

Render에 백엔드를 배포할 때 민감한 정보(API 키, 데이터베이스 키 등)는 Git에 커밋하지 않고 Render의 환경 변수 기능을 사용하여 안전하게 관리합니다.

## 🔐 환경 변수가 필요한 이유

- **보안**: API 키와 비밀 키를 코드 저장소에 노출하지 않음
- **유연성**: 개발/스테이징/프로덕션 환경마다 다른 값 사용 가능
- **관리 용이**: 코드 변경 없이 환경 변수만 수정하여 배포 가능

## 🚀 Render에서 환경 변수 설정하기

### 1. Render 대시보드 접속

1. [Render Dashboard](https://dashboard.render.com) 접속
2. 배포한 백엔드 서비스 선택

### 2. Environment 탭으로 이동

1. 왼쪽 사이드바에서 **"Environment"** 클릭
2. 또는 서비스 설정 페이지에서 **"Environment" 탭** 선택

### 3. 환경 변수 추가

각 환경 변수를 다음과 같이 추가합니다:

#### 필수 환경 변수

| Key | Value (예시) | 설명 |
|-----|-------------|------|
| `SUPABASE_URL` | `https://mlbyllouvapjwfepgzeo.supabase.co` | Supabase 프로젝트 URL |
| `SUPABASE_SERVICE_ROLE_KEY` | `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...` | Supabase Service Role Key |
| `PERPLEXITY_API_KEY` | `pplx-JxtIsxegxw0Qg3uyIi70...` | Perplexity API 키 |
| `PERPLEXITY_DEFAULT_MODEL` | `sonar` | Perplexity 기본 모델 |
| `ENABLE_SERVER_SAVE` | `true` | 서버 저장 활성화 |

### 4. 환경 변수 입력 방법

#### 방법 1: UI에서 직접 입력 (추천)

1. **"Add Environment Variable"** 버튼 클릭
2. **Key** 필드에 변수명 입력 (예: `PERPLEXITY_API_KEY`)
3. **Value** 필드에 값 입력
4. **"Save Changes"** 클릭

![Render Environment Variables](https://docs.render.com/images/environment-variables.png)

#### 방법 2: .env 파일 업로드

1. **"Add from .env"** 버튼 클릭
2. 로컬의 `.env` 파일 내용을 복사하여 붙여넣기
3. **"Save Changes"** 클릭

```bash
# 복사할 내용 예시 (.env 파일에서)
SUPABASE_URL=https://mlbyllouvapjwfepgzeo.supabase.co
SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
PERPLEXITY_API_KEY=pplx-JxtIsxegxw0Qg3uyIi70...
PERPLEXITY_DEFAULT_MODEL=sonar
ENABLE_SERVER_SAVE=true
```

### 5. 환경 변수 적용

환경 변수를 추가/수정하면 **자동으로 서비스가 재배포**됩니다.
- 재배포 진행 상황은 "Events" 탭에서 확인 가능
- 일반적으로 1-3분 소요

## 📝 단계별 상세 가이드

### Step 1: Perplexity API 키 발급

1. [Perplexity AI Settings](https://www.perplexity.ai/settings/api) 접속
2. **"API Keys"** 섹션으로 이동
3. **"Create API Key"** 클릭
4. 생성된 키 복사 (예: `pplx-xxxxxxxxxxxxxxxxxxxx`)
5. **⚠️ 중요**: 생성 직후에만 표시되므로 반드시 안전한 곳에 저장!

### Step 2: Supabase 키 확인

1. [Supabase Dashboard](https://supabase.com/dashboard) 접속
2. 프로젝트 선택
3. 왼쪽 메뉴에서 **"Project Settings"** → **"API"** 클릭
4. 다음 정보 복사:
   - **URL**: Project URL
   - **service_role key**: Service role (secret)

### Step 3: Render에 환경 변수 추가

```
# Render Dashboard → Your Service → Environment 탭

1. SUPABASE_URL 추가
   Key: SUPABASE_URL
   Value: [Supabase Project URL]

2. SUPABASE_SERVICE_ROLE_KEY 추가
   Key: SUPABASE_SERVICE_ROLE_KEY
   Value: [Supabase Service Role Key]

3. PERPLEXITY_API_KEY 추가
   Key: PERPLEXITY_API_KEY
   Value: [Perplexity API Key]

4. PERPLEXITY_DEFAULT_MODEL 추가
   Key: PERPLEXITY_DEFAULT_MODEL
   Value: sonar

5. ENABLE_SERVER_SAVE 추가
   Key: ENABLE_SERVER_SAVE
   Value: true
```

### Step 4: 환경 변수 확인

배포 완료 후 로그에서 환경 변수가 제대로 로드되었는지 확인:

```bash
# Render 로그 예시
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:10000
✅ Environment variables loaded
✅ Perplexity API key: pplx-****...****
✅ Supabase connected
```

## 🔒 보안 모범 사례

### 1. .env 파일 보호

```bash
# .gitignore에 반드시 포함 (이미 포함되어 있음)
.env
.env.local
.env.*.local
```

### 2. 환경 변수 확인 코드

`app/main.py` 또는 설정 파일에서:

```python
import os
from dotenv import load_dotenv

# .env 파일 로드 (로컬 개발용)
load_dotenv()

# 필수 환경 변수 확인
REQUIRED_ENV_VARS = [
    "SUPABASE_URL",
    "SUPABASE_SERVICE_ROLE_KEY",
    "PERPLEXITY_API_KEY",
]

for var in REQUIRED_ENV_VARS:
    if not os.getenv(var):
        raise ValueError(f"❌ Required environment variable {var} is not set!")
    print(f"✅ {var}: {'*' * 10}...{'*' * 4}")
```

### 3. API 키 로테이션

정기적으로 API 키를 갱신하세요:
- Perplexity: 6개월마다
- Supabase: 1년마다 또는 유출 의심 시 즉시

### 4. 최소 권한 원칙

각 환경에 필요한 최소한의 권한만 부여:
- 개발 환경: 제한된 권한의 API 키
- 프로덕션: 필요한 모든 권한

## 🛠️ 트러블슈팅

### 문제 1: 환경 변수가 적용되지 않음

**증상**: 배포 후에도 환경 변수를 찾을 수 없다는 오류

**해결 방법**:
1. Render 대시보드에서 환경 변수가 제대로 저장되었는지 확인
2. 변수명의 오타 확인 (대소문자 구분)
3. 수동으로 **"Manual Deploy"** 클릭하여 재배포

### 문제 2: API 키가 유효하지 않음

**증상**: 401 Unauthorized 또는 403 Forbidden 오류

**해결 방법**:
1. Perplexity/Supabase 대시보드에서 키가 활성화되어 있는지 확인
2. 키를 재생성하고 Render에 업데이트
3. 키 앞뒤의 공백 제거 확인

### 문제 3: 로컬에서는 작동하는데 Render에서 오류

**증상**: 로컬 개발 환경에서는 정상, 프로덕션에서만 오류

**해결 방법**:
1. `.env.example` 파일과 Render 환경 변수 비교
2. 모든 필수 변수가 Render에 설정되었는지 확인
3. Render 로그 확인: Dashboard → Your Service → Logs

### 문제 4: 재배포 후에도 변경사항이 반영되지 않음

**해결 방법**:
```bash
# Render Dashboard에서
1. "Manual Deploy" → "Clear build cache & deploy" 선택
2. 또는 Environment 변수를 임시로 변경했다가 원래대로 되돌리기
```

## 📊 환경 변수 관리 팁

### 1. 환경별 분리

```
개발 환경 (.env.local):
- 테스트용 API 키
- 로컬 데이터베이스

프로덕션 (Render):
- 프로덕션 API 키
- 프로덕션 데이터베이스
```

### 2. 문서화

`docs/ENVIRONMENT_VARIABLES.md` 파일 생성:

```markdown
# 환경 변수 목록

## 필수 변수
- `PERPLEXITY_API_KEY`: Perplexity AI API 키
- `SUPABASE_URL`: Supabase 프로젝트 URL
- ...

## 선택 변수
- `LOG_LEVEL`: 로그 레벨 (기본값: INFO)
- ...
```

### 3. 백업

중요한 환경 변수는 안전한 곳에 백업:
- 암호 관리자 (1Password, LastPass 등)
- 팀 공유 문서 (Google Docs, Notion 등) - 접근 제한 설정
- 시크릿 관리 서비스 (AWS Secrets Manager, Vault 등)

## ✅ 체크리스트

배포 전 확인사항:

- [ ] `.env` 파일이 `.gitignore`에 포함되어 있음
- [ ] `.env.example` 파일이 최신 상태로 유지됨
- [ ] 모든 필수 환경 변수가 Render에 설정됨
- [ ] API 키가 유효하고 활성화되어 있음
- [ ] 로컬에서 정상 작동 확인
- [ ] Render 배포 후 로그 확인
- [ ] API 엔드포인트 테스트

## 🔗 유용한 링크

- [Render 환경 변수 공식 문서](https://docs.render.com/environment-variables)
- [Perplexity API 문서](https://docs.perplexity.ai/)
- [Supabase 문서](https://supabase.com/docs)
- [Python-dotenv 문서](https://pypi.org/project/python-dotenv/)

## 📞 문제 해결이 안 될 때

1. Render 로그 확인: `Dashboard → Your Service → Logs`
2. Render 지원팀 문의: [Render Support](https://render.com/support)
3. 커뮤니티 포럼: [Render Community](https://community.render.com/)

---

**마지막 업데이트**: 2025년 12월 7일
