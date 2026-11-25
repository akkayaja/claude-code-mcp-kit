"""정답 예시: 학습일지 MCP 서버 (읽기 전용)

미션을 직접 해 본 뒤 비교할 때만 열어요.

- 공식 MCP 파이썬 SDK 2.x 기준 (`pip install "mcp[cli]"`, 파이썬 3.10 이상)
  * 1.x 때 이름은 FastMCP(`from mcp.server.fastmcp import FastMCP`)였고,
    2.x에서 MCPServer로 바뀌었어요. 인터넷 예제가 FastMCP라면 옛날 버전이에요.
- 학습일지 폴더는 환경변수 STUDY_LOG_DIR로 정해요. 없으면 이 파일 옆의 샘플_학습일지/를 써요.
- 도구 이름은 영어로 해요. Claude가 받는 도구 이름은 영문·숫자·_·- 만 쓸 수 있어서예요.
  대신 title(제목)과 설명은 한국어로 달아요.
"""

import os
import re
from collections import Counter
from datetime import date
from pathlib import Path

from mcp.server import MCPServer

LOG_DIR = Path(
    os.environ.get("STUDY_LOG_DIR", Path(__file__).parent / "샘플_학습일지")
).expanduser().resolve()

mcp = MCPServer(
    "study-log",
    instructions="내 학습일지 폴더(마크다운 파일)를 읽기만 하는 서버예요. 파일을 만들거나 고치지 않아요.",
)


def _logs() -> list[Path]:
    """학습일지 폴더의 .md 파일 목록 (이름순)."""
    if not LOG_DIR.is_dir():
        return []
    return sorted(p for p in LOG_DIR.glob("*.md") if p.is_file())


def _date_of(text: str) -> str:
    """'- **날짜:** 2026-11-10' 줄에서 날짜만 꺼내요. 없으면 빈 글자."""
    m = re.search(r"날짜:\**\s*(\d{4}-\d{2}-\d{2})", text)
    return m.group(1) if m else ""


def _section(text: str, title_word: str) -> list[str]:
    """'## 🔌 연결한 MCP' 같은 제목 아래의 '- 항목' 줄들을 꺼내요."""
    items: list[str] = []
    inside = False
    for line in text.splitlines():
        if line.startswith("## "):
            inside = title_word in line
            continue
        if inside and line.strip().startswith("- "):
            items.append(line.strip()[2:].strip())
    return items


@mcp.tool(title="오늘_기록_목록")
def list_logs_by_date(day: str = "") -> str:
    """특정 날짜(YYYY-MM-DD)의 학습일지 목록을 보여 줘요. 비우면 오늘 날짜예요.
    그날 기록이 없으면 가장 최근 기록 3개를 대신 알려 줘요."""
    target = day.strip() or date.today().isoformat()
    rows = []
    for p in _logs():
        d = _date_of(p.read_text(encoding="utf-8"))
        rows.append((d, p.name))
    hits = [name for d, name in rows if d == target]
    if hits:
        return f"{target} 기록 {len(hits)}개:\n" + "\n".join(f"- {n}" for n in hits)
    recent = sorted((r for r in rows if r[0]), reverse=True)[:3]
    lines = "\n".join(f"- {d} {n}" for d, n in recent) or "- (기록 없음)"
    return f"{target} 기록은 없어요. 최근 기록:\n{lines}"


@mcp.tool(title="키워드로_찾기")
def search_logs(keyword: str, max_results: int = 20) -> str:
    """학습일지 전체에서 키워드가 들어간 줄을 찾아 '파일 이름: 줄' 모양으로 보여 줘요.
    대소문자는 구분하지 않아요."""
    word = keyword.strip()
    if not word:
        return "찾을 키워드를 알려 주세요."
    found = []
    for p in _logs():
        for no, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
            if word.lower() in line.lower():
                found.append(f"{p.name}:{no}: {line.strip()}")
    if not found:
        return f"'{word}'가 들어간 기록이 없어요."
    more = f"\n…외 {len(found) - max_results}줄 더" if len(found) > max_results else ""
    return f"'{word}' {len(found)}줄 찾음:\n" + "\n".join(found[:max_results]) + more


@mcp.tool(title="진도_요약")
def progress_summary(total_lessons: int = 32) -> str:
    """지금까지의 진도를 요약해요: 기록한 강의 수, 강의 번호, 첫·마지막 날짜, 연결한 MCP 횟수."""
    logs = _logs()
    if not logs:
        return f"학습일지 폴더에 기록이 없어요: {LOG_DIR.name}"
    numbers, dates, mcps = [], [], Counter()
    for p in logs:
        text = p.read_text(encoding="utf-8")
        m = re.match(r"(\d+)_", p.name)
        if m:
            numbers.append(int(m.group(1)))
        if d := _date_of(text):
            dates.append(d)
        for item in _section(text, "연결한 MCP"):
            name = re.split(r"[\s(]", item)[0]
            if name and name != "없음":
                mcps[name] += 1
    done = sorted(set(numbers))
    pct = round(len(done) / total_lessons * 100)
    lines = [
        f"기록한 강의: {len(done)}개 / {total_lessons}개 ({pct}%)",
        "강의 번호: " + ", ".join(f"{n:02d}" for n in done),
        f"기간: {min(dates)} ~ {max(dates)}" if dates else "기간: (날짜 없음)",
        "연결한 MCP: " + (", ".join(f"{k} {v}회" for k, v in mcps.most_common()) or "없음"),
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run()  # 기본은 stdio: Claude Code가 이 프로그램을 켜고 표준 입출력으로 대화해요
