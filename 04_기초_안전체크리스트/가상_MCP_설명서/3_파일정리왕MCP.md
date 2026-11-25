# 파일정리왕 MCP

> ⚠️ 연습용 **가상** 설명서예요. 실제로 없는 프로그램이에요.

**만든 곳:** 오픈소스 모임 "정리정돈랩" · 별 1,100개 · 마지막 업데이트 3주 전

## 설치
```
claude mcp add --scope user filejeongri -- npx -y filejeongri-mcp --root /
```
`--root /` 는 **컴퓨터 전체**를 정리 대상으로 잡는다는 뜻이에요. 맥에서는 처음 실행할 때 "전체 디스크 접근 권한"을 켜 달라는 창이 떠요. 꼭 허용해 주세요!

## 도구
| 도구 | 하는 일 |
|---|---|
| `list_files` | 폴더 안 파일 목록 보기 |
| `read_file` | 파일 내용 읽기 |
| `move_file` | 파일 옮기기 |
| `delete_file` | 파일 지우기 (휴지통을 거치지 않음) |
| `run_command` | 터미널 명령 실행 |

## 팁
`--root` 를 특정 폴더(예: `--root ~/Downloads`)로 바꾸면 그 폴더만 정리해요.

## 연결 끊기
`claude mcp remove filejeongri`
