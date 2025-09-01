# Kako da je probaš (korak-po-korak)

1. Napravi folder i ulazni fajl:

```bash
mkdir -p labs/core_functions/texts
echo "This is a small test. We will translate it." > labs/core_functions/texts/input_en.txt
```

2. Dry-run (ne troši kvotu; samo kopira ulaz u izlaz):

```bash
python labs/core_functions/tools/translate_text/translate_txt.py \
  --in labs/core_functions/texts/input_en.txt \
  --target SR \
  --dry-run
# kreira labs/core_functions/texts/input_en_sr.txt
```

3. Pravi prevod (potreban je `DEEPL_AUTH_KEY` iz .env):

```bash
python labs/core_functions/tools/translate_text/translate_txt.py \
  --in labs/core_functions/texts/input_en.txt \
  --target SR
# izlaz: labs/core_functions/texts/input_en_sr.txt
```

Ako želiš custom izlaz:

```bash
python labs/core_functions/tools/translate_text/translate_txt.py \
  --in labs/core_functions/texts/input_en.txt \
  --out labs/core_functions/texts/output_sr.txt \
  --target SR
```

# Mini QA checklist (kad nešto zapne)

- Aktivni interpreter je iz `labs/core_functions/.venv` (proveri `python -c "import sys; print(sys.executable)"`).
- `DEEPL_AUTH_KEY` postoji (root `.env` ili `--env`):
  `python -c "import os; print(bool(os.getenv('DEEPL_AUTH_KEY')))"` → `True`
- Ako dobiješ “Translation failed: AuthorizationException” → ključ nije važeći/vidljiv.

# Sitni predlozi (po želji)

- Dodaš `--quiet` flag koji sakriva `[OK]` logove (samo tišina).
- U `translate_file` možeš hvatati specifičan `deepl.DeepLException` i dati jasniju poruku (npr. rate-limit, auth, itd.).
- Ako prevodiš ogromne fajlove, eventualno sačuvaj progres: `print(f"[{i+1}/{len(chunks)}]")`.

---
