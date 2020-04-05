import json


class Pdf2TextEncoder(json.JSONEncoder):

    def default(self, o):
        try:
            to_serialize = {
                'patient_id': o.patient_id,
                "document_text": str(o.document_text)
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
