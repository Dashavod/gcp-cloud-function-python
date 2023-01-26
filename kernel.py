import openai
from contentFilter import filter_content
import os

SENSITIVE_DATA = 'You request contans sensitive data. Please change request'
openai_api_key = "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"#os.getenv('OPENAI_API_KEY')


ENGINE_NAME = 'text-davinci-003'
openai.api_key = openai_api_key


def kernel(
    prompt: str,
    user_id: str,
    temp: float,
    max_tokens=250,
    min_output=50,
    max_tries=3,
    presence_penalty=0.6,
    frequency_penalty=0.0,
    stop_words=None,
    disable_filter=False
) -> str:
    tries = 0

    if not filter_content(prompt, str(user_id)):
        raise Exception(SENSITIVE_DATA)

    while tries < max_tries:
        resp = openai.Completion.create(
            user=user_id,
            engine=ENGINE_NAME,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temp,
            top_p=1,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            stop=stop_words
        )

        tries = tries + 1
        print(resp)
        choices = resp['choices']
        if len(choices) > 0:
            result = choices[0]['text'].strip()

            if len(result) > min_output:
                if disable_filter or filter_content(result, str(user_id)):
                    return result

    return ''
