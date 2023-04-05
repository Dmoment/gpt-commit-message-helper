# GPT-Commit-Message-Helper

Automatically generate and suggest context-aware Git commit messages using OpenAI's GPT. This repository provides an easy-to-integrate solution to streamline your commit process and enhance commit message quality.

## Prerequisites

- Python 3
- OpenAI API key

## Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/gpt-commit-message-helper.git
cd gpt-commit-message-helper
```

2. Install the required Python packages:

```bash
pip install openai
```

3. Set your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY=your_api_key_here
```

4. Copy the `commit_with_suggestion.sh` script to your target Git repository's root directory.

5. Make the script executable:

```bash
chmod +x commit_with_suggestion.sh
```

6. Create a Git alias to run the script. Run the following command in your terminal:

```bash
git config --global alias.scommit '!sh ./commit_with_suggestion.sh'
```

## Usage

Instead of using `git commit`, use `git scommit` in your repository. This command will run the custom script, which will prompt you for the commit message with the GPT-generated suggestion. You can press ENTER to use the suggested commit message or type a custom one and press ENTER.

Example:

```bash
git add .
git scommit
```

## How it works

When you run the git commit command, Git passes the changes that are staged for commit to the pre-commit hook, which is located in the .git/hooks/ directory. The commit_with_suggestion.sh script is a pre-commit hook that runs the gpt_commit_message.py script to generate a commit message based on the changes.

The gpt_commit_message.py script takes the file paths of the changed files as command line arguments and generates a commit message by using OpenAI's GPT-3 API. The script first generates a summary of the changes made to each file by getting the Git diff of the file and extracting the added/modified lines from the diff. It then combines the first three lines of added/modified content to form a summary.

The gpt_commit_message.py script then sends a prompt to the GPT-3 API that includes the file names and summaries of the changed files. The API generates a commit message based on the prompt and returns it to the script.

The commit_with_suggestion.sh script then displays the suggested commit message and prompts the user to either use the suggested message by pressing ENTER or enter a custom message. If the user enters a custom message, the script uses that message for the commit. Otherwise, it uses the suggested message.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
