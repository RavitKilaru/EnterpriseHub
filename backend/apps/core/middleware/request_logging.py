import logging
import time

logger = logging.getLogger("django.request")


class RequestLoggingMiddleware:
    """
    Logs every HTTP request and response.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start_time = time.perf_counter()

        response = self.get_response(request)

        duration = (time.perf_counter() - start_time) * 1000

        logger.info(
            (
                "RequestID=%s | "
                "Method=%s | "
                "Path=%s | "
                "Status=%s | "
                "Duration=%.2fms | "
                "IP=%s | "
                "User=%s"
            ),
            getattr(request, "request_id", "-"),
            request.method,
            request.get_full_path(),
            response.status_code,
            duration,
            request.META.get("REMOTE_ADDR"),
            request.user if getattr(request, "user", None) and request.user.is_authenticated else "Anonymous",
        )

        return response