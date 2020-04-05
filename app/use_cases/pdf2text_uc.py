from app.shared import use_case as uc
from app.shared import response_obj as res


class PdfToTextUseCase(uc.UseCase):

    def __init__(self, repo):
        self.repo = repo

    def process_request(self, file):
        response = self.repo.extract_text()
        return res.ResponseSuccess(response)
