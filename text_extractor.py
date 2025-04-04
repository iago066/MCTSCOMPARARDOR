import docx2txt
class TextExtractor:
    def extract_text(self, file_path):
        try:
            return docx2txt.process(file_path)
        except:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return f.read()