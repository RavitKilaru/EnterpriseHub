import uuid


class RequestIDMiddleware:
    """
    Adds a unique request ID to every incoming HTTP request.
    """

    HEADER_NAME = "HTTP_X_REQUEST_ID"

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_id = (
            request.META.get(self.HEADER_NAME)
            or str(uuid.uuid4())
        )

        request.request_id = request_id

        response = self.get_response(request)

        response["X-Request-ID"] = request_id

        return response