import hashlib
from app.domain.file import File


def test_file_model_init():
    patient_id = hashlib.md5(str(1000).encode()).hexdigest()
    doc_text = "ABCDE"
    file = File(patient_id=patient_id, document_text=doc_text)
    assert file.patient_id == patient_id
    assert file.document_text == doc_text


def test_file_model_from_dict():
    patient_id = hashlib.md5(str(1000).encode()).hexdigest()
    doc_text = "ABCDE"
    file = File.from_dict(
        {
            'patient_id': patient_id,
            'document_text': doc_text
        }
    )
    assert file.patient_id == patient_id
    assert file.document_text == doc_text


def test_file_model_to_dict():
    patient_id = hashlib.md5(str(1000).encode()).hexdigest()
    doc_text = "ABCDE"
    file_dict = {
        'patient_id': patient_id,
        'document_text': doc_text
    }

    file = File.from_dict(file_dict)
    assert file.to_dict() == file_dict


def test_file_model_comparison():
    patient_id = hashlib.md5(str(1000).encode()).hexdigest()
    doc_text = "ABCDE"
    file_dict = {
        'patient_id': patient_id,
        'document_text': doc_text
    }
    file_1 = File.from_dict(file_dict)
    file_2 = File.from_dict(file_dict)

    assert file_1 == file_2
