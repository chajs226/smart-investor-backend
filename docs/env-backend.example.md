### Backend .env example

```
# Supabase
SUPABASE_URL=
SUPABASE_SERVICE_ROLE_KEY=

# Perplexity API (필수)
PERPLEXITY_API_KEY=your-perplexity-api-key-here
PERPLEXITY_DEFAULT_MODEL=sonar-deep-research

# (Optional) Logging
LOG_LEVEL=INFO
```

Notes:
- 백엔드에서는 서비스 롤 키로 삽입을 수행합니다. 키는 절대 클라이언트에 노출하지 않습니다.
- `PERPLEXITY_API_KEY`: Perplexity API 키 (필수). https://www.perplexity.ai/settings/api 에서 발급
- `PERPLEXITY_DEFAULT_MODEL`: 기본 모델명 (선택). 미설정 시 `sonar-deep-research` 사용

