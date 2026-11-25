# 16. 깃허브

> **얻는 능력:** 메모를 Claude가 **깃허브 이슈로 정리·라벨링**하고, 진행 상황을 요약해 주는 능력

**왜 배우나요?** 프로젝트 할 일을 깃허브 이슈로 관리하면 무엇이 남았는지 한눈에 보여요. 이미 `gh` 명령으로 깃허브를 다룰 줄 알죠? 이번엔 **MCP로 다루면 뭐가 다른지** 비교해 봐요. 비유하면 `gh`는 **내가 직접 쓰는 리모컨**, 깃허브 MCP는 **Claude에게 건네준 리모컨**이에요.

## 📁 들어 있는 파일
- `이슈_원본.md` – 가상의 '독서기록 웹페이지'를 만들며 적은 메모 8개 + 라벨·제목 규칙
- `정답_라벨.md` – 라벨 나누기 정답 (**채점 전까지 열지 않기!**)

## 🔌 연결하기
연결 전에 `공통/MCP_검사표.md`로 확인해요. 깃허브가 직접 만든 **공식 원격 MCP**(`https://api.githubcopilot.com/mcp`)를 써요.

**1) 연습 저장소 만들기 (직접)** — 터미널에서:
```bash
gh repo create mcp-practice --public --add-readme
```
→ 내 계정에 `mcp-practice` 저장소를 README와 함께 새로 만들어요.

**2) 토큰(PAT) 만들기 (직접)** — 깃허브 → Settings → Developer settings → **Fine-grained tokens** → Generate
- Repository access: **Only select repositories → `mcp-practice` 하나만**
- Permissions: **Issues: Read and write** (Metadata: Read는 자동). 다른 건 켜지 않아요. 만료일은 7일.
- 토큰은 키트 폴더의 `.env`에 `GITHUB_PAT=...` 한 줄로 **내가 직접** 붙여 넣어요. 채팅에는 절대 붙여 넣지 않아요.

**3) 이 폴더에서만 연결** — 키트 폴더에서 직접 실행해요.
```bash
claude mcp add-json --scope project github '{"type":"http","url":"https://api.githubcopilot.com/mcp","headers":{"Authorization":"Bearer ${GITHUB_PAT}"}}'
```
→ `.mcp.json`에 연결 정보를 쓰는데, 키 자리에는 **`${GITHUB_PAT}`라는 이름표만** 들어가요. 진짜 키는 `.env`에만 있어요. (작은따옴표 덕분에 이름표가 그대로 저장돼요.)
```bash
export GITHUB_PAT="$(grep '^GITHUB_PAT=' .env | cut -d '=' -f2-)"
claude
```
→ `.env`에서 키를 읽어 이 터미널에만 잠깐 올려 두고 Claude Code를 켜요. `/mcp`에서 github가 ✔인지 확인해요.

공식 안내: https://github.com/github/github-mcp-server/blob/main/docs/installation-guides/install-claude.md · 키 이름표(`${VAR}`): https://code.claude.com/docs/en/mcp
(명령 형식은 Claude Code 버전에 따라 달라요. 안 되면 공식 문서에서 최신 방법을 확인해요.)

## ⚠️ 알아 둘 것
- 토큰은 **열쇠**예요. 저장소 하나, 이슈 권한 하나만 준 열쇠라서 잃어버려도 피해가 작아요. 다 쓰면 깃허브에서 **토큰 삭제**해요.
- 이슈 **닫기·삭제**, 저장소 설정 변경, 다른 저장소 작업은 시키지 않아요.
- 공개 저장소예요. 이슈에 개인정보·회사 이야기를 쓰지 않아요.
- 끝나면 `claude mcp remove github -s project`로 지울 수 있어요.

## 🧭 기본 미션 (순서대로)
1. `이슈_원본.md` 맨 아래 "내가 먼저 예상해 볼 것"을 직접 채운다
2. 연습 저장소·토큰·연결을 위 순서대로 직접 한다
3. Claude에게 **만들 이슈 8개와 라벨을 표로 먼저** 받고, 확인한 뒤 `mcp-practice`에 이슈를 만들게 한다 (`급함` 라벨도 새로)
4. 깃허브 웹에서 이슈 8개와 라벨을 직접 확인한다
5. 터미널에서 같은 내용을 `gh`로 확인해 본다
   ```bash
   gh issue list --repo 내아이디/mcp-practice --label 급함
   ```
   → `급함` 라벨이 붙은 이슈만 목록으로 보여 줘요.
6. Claude에게 **진행 상황 요약**(라벨별 개수, 급한 것 먼저)을 받아 `결과/이슈_요약.md`로 저장하고, `정답_라벨.md`로 채점한다

## 🔥 도전 미션 (기본을 끝냈다면)
- 내가 웹에서 이슈 2개를 직접 닫은 뒤, "남은 이슈"를 다시 요약받기
- `gh`와 MCP 비교표 만들기: 같은 일(이슈 목록 보기)을 할 때 **빠르기 / 정확성 / 내가 이해하는 정도**

## 💬 Claude Code에 이렇게 말해 보세요
막히면 그대로 복사해서 써도 돼요. 단, **먼저 결과를 직접 보고, 모르는 건 "이게 무슨 뜻이야?"라고 꼭 물어보세요.**

```
깃허브 MCP로 내 'mcp-practice' 저장소만 다룰 거야. 다른 저장소는 읽거나 고치지 마. 지금 이 저장소의 이슈와 라벨 목록을 보여 줘.
```
```
이슈_원본.md를 읽고, 규칙대로 이슈 제목·본문·라벨을 표로 만들어 줘. 아직 만들지 마.
```
```
좋아. 'mcp-practice'에 '급함' 라벨을 주황색으로 만들고, 표대로 이슈 8개를 만들어 줘. 만든 이슈 번호를 알려 줘.
```
```
이 저장소의 열린 이슈를 라벨별로 세고, 급한 것부터 3줄로 진행 상황을 요약해 줘.
```

## ✅ 완료 체크리스트
- [ ] 토큰 범위를 저장소 1개·이슈 권한만으로 만들었다
- [ ] `.mcp.json`에 진짜 키가 아닌 `${GITHUB_PAT}`만 있는 걸 확인했다
- [ ] 이슈 8개와 라벨을 깃허브 웹에서 확인했다
- [ ] `gh` 명령과 MCP의 차이를 한 줄로 말할 수 있다
- [ ] 다 쓴 뒤 토큰 삭제·MCP 지우는 법을 안다

## 📝 포트폴리오 한 줄 (완료 후 채우기)
- 문제: 
- 해결: 
- 효과: 
