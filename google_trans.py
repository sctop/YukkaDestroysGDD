import requests
from pprint import pprint

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/99.0.4844.82 Safari/537.36"
}
url_google_en = "https://translate.googleapis.com/translate_a/single?client=gtx&dt=t&dt=bd&dj=1&dt=ex&dt=ld&dt=md&dt=qca&dt=rm&dt=ss&sl=auto&tl=en&q={}"

SESSION = requests.Session()

class GoogleTranslate():
    def __init__(self, keyword):
        self.keyword = keyword
        self.api_call()

    def api_call(self):
        r = SESSION.get(url_google_en.format(self.keyword), headers=headers, timeout=5)
        if r.status_code == 200:
            self.data = r.json()
        r.raise_for_status()

    def language(self):
        return ",".join(self.data["ld_result"]["extended_srclangs"])


t = GoogleTranslate("")
pprint(t.data["ld_result"]["extended_srclangs"])
