from app.shared import response_obj as res


class UseCase(object):

    def execute(self, file):
        if not file:
            return res.ResponseFailure.build_from_invalid_file(file)

        try:
            return self.process_request(file)
        except Exception as exc:
            return res.ResponseFailure.build_system_error(
                "{}: {}".format(exc.__class__.__name__, "{}".format(exc)))

    def process_request(self, file):
        raise NotImplementedError("process_request() not implemented by UseCase class")
