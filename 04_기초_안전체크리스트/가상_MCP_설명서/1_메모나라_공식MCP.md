# 메모나라 MCP (공식)

> ⚠️ 연습용 **가상** 설명서예요. 메모나라는 실제로 없는 서비스예요.

**만든 곳:** 메모나라 주식회사 (메모나라 공식 개발 문서 `docs.memonara.example/mcp`에 안내)
**저장소:** `github.com/memonara-official/memonara-mcp` · 별 4,200개 · 마지막 업데이트 9일 전 · 열린 이슈 12개 (대부분 답변 있음)

## 연결 방법
원격(HTTP) 연결이에요. 설치할 프로그램이 없어요.
```
claude mcp add --transport http --scope project memonara https://mcp.memonara.example/mcp
```
처음 쓸 때 메모나라 로그인 창이 뜨고, 허용할 권한을 직접 고를 수 있어요.

## 도구
| 도구 | 하는 일 |
|---|---|
| `search_notes` | 메모 검색 |
| `read_note` | 메모 읽기 |
| `create_note` | 새 메모 만들기 |
| `update_note` | 메모 고치기 |

메모 **삭제와 공유 링크 만들기는 MCP로 할 수 없어요.** 앱에서 직접 해 주세요.

## 권한 범위
로그인할 때 "모든 메모" 또는 "고른 폴더만" 중에서 고를 수 있어요.

## 연결 끊기
메모나라 앱 → 설정 → 연결된 앱 → Claude → 연결 해제
