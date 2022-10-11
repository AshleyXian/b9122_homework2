import re


def find_word(soup, target_word):
    pattern = f'.*?({target_word}).*?'
    for p in soup.find_all('p'):
        text = p.get_text()
        text = text.strip().lower()
        res = re.findall(pattern, text, re.S)
        if len(res) > 0:
            return True
    return False
