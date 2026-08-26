#!/bin/sh

if [ "$#" -gt 0 ]; then
  command_text=$*
else
  input=$(cat)

  if command -v jq >/dev/null 2>&1; then
    command_text=$(printf '%s' "$input" | jq -r '.tool_input.command // .tool_input.cmd // empty' 2>/dev/null)
  else
    command_text=$(printf '%s' "$input" | sed -n 's/.*"\(command\|cmd\)"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\2/p')
  fi

  [ -n "$command_text" ] || command_text=$input
fi

if printf '%s\n' "$command_text" | grep -Eiq 'rm[[:space:]]+-rf([[:space:]]|$)|git[[:space:]]+push[[:space:]]+--force([[:space:]]|$)|git[[:space:]]+reset[[:space:]]+--hard([[:space:]]|$)|DROP[[:space:]]+TABLE'; then
  printf '%s\n' 'BLOCKED: 위험한 명령어가 감지되었습니다'
  exit 1
fi

exit 0
