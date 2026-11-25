# 03. 설치와 해제

> **얻는 능력:** MCP를 **꽂고(add) → 확인하고 → 쓰고 → 끄고 → 뽑는(remove)** 한 바퀴를 혼자 할 수 있는 능력

**왜 배우나요?** 앞으로 MCP를 20개 넘게 연결해요. 꽂는 법만 알고 뽑는 법을 모르면 콘센트가 계속 늘어나요. 위험이 거의 없는 **공식 연습용 MCP "time"(시간 알려 주기)**으로 한 바퀴를 먼저 돌아 봐요.

## 📁 들어 있는 파일
- `실습기록_양식.md` – 단계마다 본 화면을 적는 칸. 복사해서 `결과/03_기록.md`로 써요

## 🔌 연결하기
**time**은 MCP를 만든 곳(modelcontextprotocol)이 직접 만든 **참고용 공식 서버**예요. 도구는 `get_current_time`(지금 몇 시), `convert_time`(시차 바꾸기) 같은 것뿐이라 파일도 인터넷도 건드리지 않아요.
1. **검사표로 먼저 확인:** `공통/MCP_검사표.md`를 같이 채워요 (출처: modelcontextprotocol/servers 공식 저장소)
2. 터미널에서 **이 키트 폴더(맨 위 폴더)**로 이동한 다음, 직접 실행해요.
   ```bash
   claude mcp add --scope project time -- uvx mcp-server-time --local-timezone=Asia/Seoul
   ```
   - `claude mcp add` : 콘센트를 새로 꽂아요
   - `--scope project` : **이 폴더에서만** 쓰이게. 폴더에 `.mcp.json` 파일이 생겨요
   - `time` : 내가 붙이는 이름
   - `--` 뒤 : 실제로 실행할 프로그램 (`uvx`가 time 서버를 받아서 켜요)
3. Claude Code를 다시 켜면 **"이 프로젝트 MCP를 쓸까요?"** 하고 물어봐요. 내가 직접 승인해요.
4. 최신 명령은 공식 문서에서 확인해요: https://github.com/modelcontextprotocol/servers/tree/main/src/time · https://code.claude.com/docs/en/mcp

## 📖 범위(scope) 3가지
| 범위 | 어디서 쓰나 | 어디에 저장 | 비유 |
|---|---|---|---|
| local (기본값) | 이 폴더에서만, 나만 | `~/.claude.json` | 내 방 콘센트 |
| project | 이 폴더에서만, 폴더를 받은 사람도 | 폴더의 `.mcp.json` | 공용 거실 콘센트 |
| user | 내 컴퓨터 모든 폴더 | `~/.claude.json` | 집 전체 멀티탭 |

## ⚠️ 알아 둘 것
- `.mcp.json`은 GitHub에 올라갈 수 있어요. **키를 절대 넣지 않아요** (키는 `.env`에, 07번에서 배워요).
- `uvx`가 없다는 오류가 나면 Claude에게 "uv 설치 확인해 줘"라고 물어보세요.
- 지우기 전에 끄기(Disable)부터 해 봐요. 끄기는 설정을 남기고, 지우기는 설정을 없애요.

## 🧭 기본 미션 (순서대로)
1. **추측 먼저:** 설치 후 폴더에 어떤 파일이 새로 생길지 짐작해 적는다
2. 위 명령으로 time을 **project 범위**로 꽂고, `cat .mcp.json`으로 생긴 파일을 열어 본다
3. `claude mcp list`와 대화창 `/mcp`에서 time과 도구 이름을 확인한다
4. Claude에게 "지금 서울 몇 시야? 뉴욕은?"이라고 묻고, 어떤 도구를 불렀는지 확인한다
5. `/mcp`에서 time을 **Disable** → 같은 질문 → 답이 어떻게 달라지는지 본다 → 다시 **Enable**
6. 뽑기: `claude mcp remove time --scope project` 실행 → `.mcp.json`과 `claude mcp list`에서 사라졌는지 확인한다

## 🔥 도전 미션
- 같은 time을 **local 범위**로 꽂아 보고, `.mcp.json`이 생기는지 안 생기는지 비교한 뒤 지우기
- 다른 공식 참고 서버(예: fetch)의 README를 읽고, 검사표로 "써도 될지" 판정만 해 보기 (설치는 안 해도 돼요)

## 💬 Claude Code에 이렇게 말해 보세요
```
claude mcp add --scope project time -- uvx mcp-server-time 명령을 단어 하나씩 뜻을 풀어서 설명해 줘. 실행은 내가 할게.
```
```
.mcp.json 파일 내용을 읽고 각 줄이 무슨 뜻인지 알려 줘.
```
```
local, project, user 범위 차이를 내 상황(이 키트 폴더에서만 연습)에 맞게 추천해 줘.
```

## ✅ 완료 체크리스트
- [ ] time MCP를 project 범위로 꽂았다
- [ ] `.mcp.json`을 열어 봤다
- [ ] `/mcp`에서 끄고 다시 켜 봤다
- [ ] `claude mcp remove`로 뽑고 사라진 걸 확인했다
- [ ] 범위 3가지를 비유로 설명할 수 있다

## 📝 포트폴리오 한 줄 (완료 후 채우기)
- 문제: 
- 해결: 
- 효과: 
