import re
import textract
import hashlib

from app.domain import file


class FileRepo:

    def __init__(self, path):
        self._text = ""
        self._path = path

    def extract_text(self):
        self._text = str(textract.process(self._path, method='tesseract', language='eng'))
        file_dict = {
            "patient_id": hashlib.md5(str(self.get_patient_id()).encode()).hexdigest(),
            "document_text": self.get_document_text()
        }
        return file.File.from_dict(file_dict)

    def get_patient_id(self):
        match = re.findall('(?<=MR: )([0-9]*)', self._text)
        if match:
            return match[0]
        return 0

    def get_document_text(self):
        return self._text[self._text.find("DIAGNOSES"): self._text.find("FOOTER")]
