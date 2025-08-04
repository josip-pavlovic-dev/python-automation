import os
from dotenv import load_dotenv
import deepl

load_dotenv()

auth_key = os.getenv("DEEPL_AUTH_KEY")

if not auth_key:
    raise ValueError("DEEPL_AUTH_KEY not found in environment variables.")

translator = deepl.Translator(auth_key)
result = translator.translate_text("Zdravo svete!", target_lang="EN-US")

if isinstance(result, list):
    for res in result:
        print(res.text)
else:
    print(result.text)

