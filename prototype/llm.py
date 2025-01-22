### Utility to integrate with LLMs
import os

def chat_openai(messages: list[str], model: str = "gpt-4o-mini") -> str:
    """
    Chat with OpenAI
    
    Args:
        messages: List of message strings to send to OpenAI
        model: OpenAI model to use, defaults to gpt-4o-mini
        
    Returns:
        str: Response from OpenAI
    """
    import openai

    # authenticate
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": msg} for msg in messages],
            temperature=0.2,  # 0 is deterministic, 1 is random
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error communicating with OpenAI: {str(e)}"


def chat_gemini(messages: list[str], model: str = "gemini-1.5-flash-latest") -> str:
    """
    Chat with Gemini with search enabled
    """
    pass

