from app.shared.domain_model import DomainModel


class File(object):

    def __init__(self, patient_id, document_text):
        self.patient_id = patient_id
        self.document_text = document_text

    @classmethod
    def from_dict(cls, adict):
        file = File(
            patient_id=adict['patient_id'],
            document_text=adict['document_text'],
        )

        return file

    def to_dict(self):
        return {
            'patient_id': self.patient_id,
            'document_text': self.document_text,
        }

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()


DomainModel.register(File)
