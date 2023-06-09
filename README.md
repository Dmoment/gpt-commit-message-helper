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

### Customization

You can customize the behavior of the script using the following environment variables:

- `GPT_COMMIT_MESSAGE_MODEL`: The OpenAI language model to use for generating commit messages. The default value is `text-davinci-002`.
- `GPT_COMMIT_MESSAGE_MAX_TOKENS`: The maximum number of tokens to generate in the commit message. The default value is `60`.
- `GPT_COMMIT_MESSAGE_TEMPERATURE`: The sampling temperature to use when generating the commit message. The default value is `0.7`.
- `GPT_COMMIT_MESSAGE_STOP`: A string or list of strings to use as stop words when generating the commit message. The default value is `None`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
