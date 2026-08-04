#!/bin/sh

printf '%s ✅ 작업 한 턴 완료\n' "$(date '+%Y-%m-%d %H:%M:%S')" >> "$CLAUDE_PROJECT_DIR/.claude/worklog.txt"
exit 0
