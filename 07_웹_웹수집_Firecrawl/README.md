# 07. 웹 수집 (Firecrawl)

> **얻는 능력:** 웹페이지를 **깔끔한 글(마크다운)과 표**로 바꿔 오고, 키를 안전하게 다루는 능력

**왜 배우나요?** 05번 Playwright는 브라우저를 한 칸씩 움직였어요. Firecrawl은 **주소만 주면 광고·메뉴를 걷어 낸 본문**을 바로 줘요. 대신 바깥 서비스라서 **계정과 API 키**가 필요해요. 키를 안전하게 다루는 법을 이번에 제대로 익혀요.

## 📁 들어 있는 파일
- `.env.example` – 키를 넣는 파일의 견본 (진짜 키는 넣지 않아요)
- `수집_대상.md` – 연습 사이트, 크레딧 아끼는 법, 수집 약속 4가지, 결과 확인표

## 🔌 연결하기
Firecrawl MCP는 **Firecrawl 회사가 직접 만든** 공식 MCP예요.
1. **검사표로 먼저 확인:** `공통/MCP_검사표.md` (출처: github.com/firecrawl/firecrawl-mcp-server)
2. **[내가 직접]** firecrawl.dev에서 무료 가입 → 대시보드에서 API 키 복사 (카드 등록 없이 무료 요금제가 있어요)
3. **[내가 직접]** 키트 맨 위 폴더에서 `cp 07_웹_웹수집_Firecrawl/.env.example .env` → `.env`를 열어 키를 붙여 넣고 저장
4. MCP 추가 (키 **이름**만 적고 값은 안 적어요. 작은따옴표를 꼭 써요):
   ```bash
   claude mcp add --env 'FIRECRAWL_API_KEY=${FIRECRAWL_API_KEY}' --scope project firecrawl -- npx -y firecrawl-mcp
   ```
   - `--env '...${FIRECRAWL_API_KEY}'` : "키는 켤 때 환경에서 읽어 와" 라는 뜻이에요. 설정 파일엔 이름표만 남아요
5. `cat .mcp.json` → 키 값이 아니라 `${FIRECRAWL_API_KEY}` 글자가 보이면 안전 ✅
6. `.env`를 불러온 뒤 Claude Code를 켜요: `set -a; source .env; set +a; claude` → 프로젝트 MCP **직접 승인**
7. 최신 명령은 공식 문서에서 확인해요: https://docs.firecrawl.dev/mcp-server · https://code.claude.com/docs/en/mcp

## ⚠️ 알아 둘 것
- **키를 채팅창에 붙여 넣지 않아요.** 실수로 붙였다면 대시보드에서 키를 지우고 새로 발급해요.
- Firecrawl 서버가 대신 읽어 오므로 05번 `localhost` 연습사이트는 못 읽어요 → `수집_대상.md`의 연습용 공개 사이트를 써요.
- 도구가 30개 넘게 있어요. 이번엔 `firecrawl_scrape`(한 쪽 읽기)만 써요. `crawl`(통째로 긁기)과 `monitor_*`(자동 반복 감시)는 크레딧을 많이 쓰니 쓰지 않아요.
- 이용 약관·robots.txt를 먼저 보고, **개인정보는 모으지 않아요.**

## 🧭 기본 미션 (순서대로)
1. **추측 먼저:** https://books.toscrape.com 을 직접 열어 1쪽에 책이 몇 권인지 세고, `/robots.txt`도 열어 본다
2. 위 연결하기 2~6단계를 한다 (키 단계는 내가 직접)
3. Claude에게 books.toscrape.com **1쪽만** 읽어 와서 `결과/책목록_1쪽.md`로 저장하게 한다
4. 그 결과에서 제목·가격·별점만 뽑아 `결과/책목록_1쪽.csv`로 만들게 한다
5. **내 눈으로 검증:** `수집_대상.md` 확인표를 채운다 (개수, 가격 2개, 쓴 크레딧)
6. 05번 Playwright와 비교: 속도, 결과의 깔끔함, 필요한 준비물을 3줄로 정리한다

## 🔥 도전 미션
- quotes.toscrape.com에서 "love" 태그 명언 1쪽만 가져와 작가별로 세어 보기
- 공공누리 등 **이용 허락이 표시된** 공개 자료 한 쪽을 골라 출처를 함께 적어 요약하기

## 💬 Claude Code에 이렇게 말해 보세요
```
firecrawl_scrape로 https://books.toscrape.com 1쪽만 마크다운으로 가져와서 결과/책목록_1쪽.md에 저장해 줘. crawl은 쓰지 말고, 시작 전에 크레딧이 얼마나 들지 먼저 말해 줘.
```
```
.mcp.json에 내 키가 그대로 적혀 있는지 확인해 줘. 키 값은 화면에 보여 주지 말고 '있다/없다'만 말해 줘.
```
```
이 사이트를 수집해도 되는지 robots.txt와 이용 약관 기준으로 같이 확인해 줘.
```

## ✅ 완료 체크리스트
- [ ] 가입과 키 발급을 내가 직접 했다
- [ ] `.env`에 키를 넣고, `.mcp.json`에는 키가 없음을 확인했다
- [ ] 1쪽을 마크다운과 CSV로 저장했다
- [ ] 확인표를 채우고 Playwright와 비교했다

## 📝 포트폴리오 한 줄 (완료 후 채우기)
- 문제: 
- 해결: 
- 효과: 
