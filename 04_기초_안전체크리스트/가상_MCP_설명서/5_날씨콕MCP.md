# 날씨콕 MCP

> ⚠️ 연습용 **가상** 설명서예요. 실제로 없는 프로그램이에요.

**만든 곳:** 개인 개발자 `weatherkok` · 별 85개 · **마지막 업데이트 3년 전**
**이슈:** 열린 이슈 47개. 최근 이슈 제목 예시: "설치하면 오류 나요", "보안 경고 뜹니다", "아직 관리하시나요?" (답변 없음)

## 설치
```
claude mcp add --scope project weatherkok -- npx -y weatherkok-mcp@0.2.1
```

## 도구
| 도구 | 하는 일 |
|---|---|
| `get_weather` | 도시 이름으로 오늘 날씨 보기 |
| `get_forecast` | 3일 예보 보기 |

읽기 도구만 있어요.

## 알림
README 맨 아래: "날씨 정보를 주던 바깥 서비스가 바뀌어서 지금은 잘 안 될 수 있어요. 시간 날 때 고칠게요."

## 연결 끊기
`claude mcp remove weatherkok`
