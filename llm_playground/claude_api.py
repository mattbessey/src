import os
import anthropic

class ClaudeAPI:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    def generate_response(self, prompt, max_tokens=1000):
        try:
            response = self.client.completions.create(
                model="claude-3-sonnet-20240229",
                prompt=prompt,
                max_tokens_to_sample=max_tokens
            )
            return {
                "completion": response.completion,
                "input_tokens": response.usage.input_tokens,
                "output_tokens": response.usage.output_tokens,
                "total_tokens": response.usage.total_tokens
            }
        except Exception as e:
            print(f"Error generating response: {e}")
            return None
