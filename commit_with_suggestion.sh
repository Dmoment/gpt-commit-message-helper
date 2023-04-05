#!/bin/sh


IFS=$'\n' read -d '' -r -a changed_files <<< "$(git diff --cached --name-only)"

if [ ${#changed_files[@]} -gt 0 ]; then
  commit_message=$(python3 gpt_commit_message.py "${changed_files[@]}")

  if [ -n "$commit_message" ]; then
      echo "Suggested commit message: $commit_message"
      echo "Press ENTER to use the suggested commit message, or type a custom one and press ENTER:"
      read user_input

      if [ -z "$user_input" ]; then
          user_input="$commit_message"
      fi
  fi
fi  

git commit -m "$user_input"
