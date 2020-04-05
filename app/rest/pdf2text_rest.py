import os
import json
from flask import Blueprint, request, Response
from werkzeug.utils import secure_filename

from app.use_cases import pdf2text_uc as uc
from app.repository import filerepo as fr
from app.shared import response_obj as res
from app.serializers import pdf2text_serializer as ser

blueprint = Blueprint('pdf2text', __name__)
FILE_PATH = os.getenv("PDF_FILE_PATH", "data/")


STATUS_CODES = {
    res.ResponseSuccess.SUCCESS: 200,
    res.ResponseFailure.RESOURCE_ERROR: 404,
    res.ResponseFailure.PARAMETERS_ERROR: 400,
    res.ResponseFailure.SYSTEM_ERROR: 500
}

ALLOWED_EXTENSIONS = {'pdf'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@blueprint.route('/pdf2text', methods=['POST'])
def pdf2text():
    f = request.files['file']
    if f.filename == '':
        f = None
    if f is None or not allowed_file(f.filename):
        return res.ResponseFailure.build_from_invalid_file(f)

    filename = secure_filename(f.filename)
    if not os.path.exists(FILE_PATH):
        os.makedirs(FILE_PATH)
    f.save(os.path.join(FILE_PATH, filename))

    repo = fr.FileRepo(os.path.join(FILE_PATH, filename))
    use_case = uc.PdfToTextUseCase(repo)
    response = use_case.execute(f)

    return Response(json.dumps(response.value, cls=ser.Pdf2TextEncoder),
                    mimetype='application/json',
                    status=STATUS_CODES[response.type])
