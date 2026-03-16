# Local LLM Setup with Ollama and smolagents

This project demonstrates running a local LLM (Qwen2:7B) using Ollama and interacting with it via the `smolagents` library.

## Setup Steps

1. **Install Ollama**
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```

2. **Pull Qwen2:7B model**
   ```bash
   ollama pull qwen2:7b
   ```

3. **Serve the model**
   ```bash
   ollama serve
   ```
   Keep this terminal open. The API will be available at `http://localhost:11434`.

4. **Create project folder**
   ```bash
   mkdir my-agent
   cd my-agent
   ```

5. **Create virtual environment**
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows: venv\Scripts\activate
   ```

6. **Install smolagents**
   ```bash
   pip install smolagents
   ```

7. **Run the agent**
   ```bash
   python agent_test.py
   ```

## Project Structure

- `agent_test.py` - Contains a static question and prints the model's response using `LiteLLMModel`

## Notes

- Ensure Ollama is running before executing the agent script
- The model runs entirely locally - no internet required after initial setup
