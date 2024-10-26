import os
import anthropic
from openai import OpenAI


class LLMCaller:
    def __init__(self, provider_name):
        if provider_name == "anthropic":
            self.client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        elif provider_name == "openai":
            self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate_response(self, prompt, max_tokens=1000):
        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20240620",
                max_tokens=max_tokens,
                messages=[{"role": "user", "content": prompt}],
            )
            return response
        except Exception as e:
            print(f"Error generating response: {e}")
            return None

    def generate_multiple_responses(self, prompts, max_tokens=1000):
        """
        Generate responses for multiple prompts.

        :param prompts: List of prompts to generate responses for
        :param max_tokens: Maximum number of tokens for each response
        :return: List of responses or None if an error occurs
        """
        responses = []
        try:
            for prompt in prompts:
                response = self.generate_response(prompt, max_tokens)
                if response:
                    responses.append(response)
                else:
                    print(f"Failed to generate response for prompt: {prompt}")
            return responses
        except Exception as e:
            print(f"Error generating multiple responses: {e}")
            return None

    def summarize_response(self, response, max_length=100):
        """
        Summarize a response to a specified maximum length.

        :param response: The response to summarize
        :param max_length: Maximum length of the summary
        :return: Summarized response
        """
        if not response:
            return None

        content = response.content if hasattr(response, "content") else str(response)
        if len(content) <= max_length:
            return content

        return content[: max_length - 3] + "..."

    def get_token_count(self, text):
        """
        Get an estimate of the number of tokens in the given text.
        This is a simple estimation and may not be 100% accurate.

        :param text: The text to estimate token count for
        :return: Estimated number of tokens
        """
        return len(text.split())

    def is_safe_content(self, text):
        """
        Check if the content is safe and doesn't contain harmful or inappropriate material.
        This is a placeholder and should be replaced with a more robust content filtering system.

        :param text: The text to check
        :return: Boolean indicating if the content is safe
        """
        unsafe_keywords = ["explicit", "violence", "hate", "illegal"]
        return not any(keyword in text.lower() for keyword in unsafe_keywords)
