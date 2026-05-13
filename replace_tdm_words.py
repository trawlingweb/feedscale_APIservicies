import os
import re

directory = '.'

replacements = {
    r'\bcaptura\b': 'indexación',
    r'\bcapturas\b': 'indexaciones',
    r'\bcapturar\b': 'indexar',
    r'\bcapturado\b': 'indexado',
    r'\bcapturados\b': 'indexados',
    r'\bcapturada\b': 'indexada',
    r'\bcapturadas\b': 'indexadas',
    r'\bscraping\b': 'procesamiento TDM',
    r'\bscrape\b': 'procesamiento',
    r'\bdescargar\b': 'obtener',
    r'\bdescarga\b': 'obtención',
    r'\bderechos de descarga\b': 'derechos de obtención',
    r'\bextracción\b': 'análisis TDM',
    r'\bextracciones\b': 'análisis TDM',
    r'\bextraer\b': 'procesar',
    r'\bextraídos\b': 'procesados',
    r'\bcrawler\b': 'indexador TDM',
    r'\bcrawlers\b': 'indexadores TDM',
    # We deliberately don't replace 'crawled' to avoid breaking the API JSON field names,
    # but we can replace the English text equivalent in md files if needed. For now, leaving 'crawled' as is.
}

def match_case(word, replacement):
    if word.isupper():
        return replacement.upper()
    elif word.istitle():
        return replacement.capitalize()
    return replacement

def replace_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    original_content = content
    
    for pattern, replacement in replacements.items():
        # Use a function to maintain case
        def repl(match):
            return match_case(match.group(0), replacement)
        content = re.sub(re.compile(pattern, re.IGNORECASE), repl, content)
        
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")

for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith('.md'):
            # Skip the basic boolean guide we just made if we want
            replace_in_file(os.path.join(root, file))

print("Replacement complete.")
