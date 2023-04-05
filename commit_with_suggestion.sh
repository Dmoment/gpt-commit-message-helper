#!/bin/sh

# Create a temporary file in the system's temporary directory
temp_file=$(mktemp)

# Gather staged changes
git diff --cached --name-status > "$temp_file"
changes=$(cat "$temp_file")

# Remove the temporary file
rm "$temp_file"

commit_message=$(python3 gpt_commit_message.py "$changes")

if [ -n "$commit_message" ]; then
    echo "Suggested commit message: $commit_message"
    echo "Press ENTER to use the suggested commit message, or type a custom one and press ENTER:"
    read user_input

    if [ -z "$user_input" ]; then
        user_input="$commit_message"
    fi
fi

git commit -m "$user_input"
