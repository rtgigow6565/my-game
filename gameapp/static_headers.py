from django.contrib.staticfiles.storage import StaticFilesStorage

class CustomStaticFilesStorage(StaticFilesStorage):
    def get_headers(self, name, *args, **kwargs):
        headers = super().get_headers(name, *args, **kwargs)
        headers["Cross-Origin-Embedder-Policy"] = "require-corp"
        headers["Cross-Origin-Opener-Policy"] = "same-origin"
        headers["X-Content-Type-Options"] = "nosniff"
        return headers
