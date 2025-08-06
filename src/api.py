from flask_openapi3 import Info
from flask_openapi3 import OpenAPI
from flask_cors import CORS
import os

from controller import api_view


def create_app(test_config=None):
    info = Info(title="Counter API", version="1.0.0")
    app = OpenAPI(__name__, info=info)

    app.register_api(api=api_view)

    CORS(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host=os.getenv("SERVER_NAME", "0.0.0.0"), port=5000)

    import os
