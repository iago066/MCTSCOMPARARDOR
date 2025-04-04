import re
class PublicationExtractor:
    def __init__(self):
        self.case_number_pattern = r'\d{7}-\d{2}\.\d{4}\.\d{1,2}\.\d{2}\.\d{4}'

    def extract_publications(self, text, case_numbers):
        if not text or not case_numbers:
            return {}
        publications = {}
        text = text.replace('\r\n', '\n').replace('\r', '\n')
        for case_number in case_numbers:
            for match in re.finditer(re.escape(case_number), text):
                context = text[max(0, match.start()-2000):match.start()+3000].strip()
                publications[case_number] = {
                    'processo': case_number,
                    'texto_completo': context
                }
        return publications