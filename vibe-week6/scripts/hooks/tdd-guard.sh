#!/bin/sh

input=$(cat)

if command -v jq >/dev/null 2>&1; then
  file_path=$(printf '%s' "$input" | jq -r '.tool_input.file_path // empty' 2>/dev/null)
else
  file_path=$(printf '%s' "$input" | sed -n 's/.*"file_path"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')
fi

[ -n "$file_path" ] || exit 0

file_name=${file_path##*/}
case "$file_name" in
  *test*|*.md|*.json|*.yml) exit 0 ;;
esac

project_dir=${CLAUDE_PROJECT_DIR:-$(pwd)}
relative_path=${file_path#"$project_dir"/}

case "$relative_path" in
  src/*.js)
    base_name=${file_name%.js}
    source_dir=${relative_path%/*}
    root_test="$project_dir/tests/$base_name.test.js"
    local_test="$project_dir/$source_dir/$base_name.test.js"

    if [ ! -f "$root_test" ] && [ ! -f "$local_test" ]; then
      escaped_name=$(printf '%s' "$base_name" | sed 's/\\/\\\\/g; s/"/\\"/g')
      printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"TDD GUARD: %s 테스트가 없습니다. 테스트를 먼저 작성하세요 (예: tests/%s.test.js)"}}\n' "$escaped_name" "$escaped_name"
    fi
    ;;
esac

exit 0
