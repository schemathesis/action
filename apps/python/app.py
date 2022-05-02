from flask import Flask
from werkzeug.exceptions import InternalServerError

app = Flask("test_app")


@app.route("/openapi.json")
def schema():
    return {
        "openapi": "3.0.2",
        "info": {
            "title": "Example API",
            "description": "An API to test Schemathesis Action",
            "version": "1.0.0",
        },
        "paths": {
            "/success": {
                "get": {
                    "responses": {
                        "200": {
                            "description": "OK",
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "type": "object",
                                        "properties": {"success": {"type": "boolean"}},
                                        "required": ["success"],
                                    }
                                }
                            },
                        }
                    }
                }
            },
            "/failure": {"get": {"responses": {"200": {"description": "OK"}}}},
        },
        "servers": [
            {
                "url": "https://example.schemathesis.io/{basePath}",
                "variables": {"basePath": {"default": "api"}},
            }
        ],
    }


@app.route("/api/success", methods=["GET"])
def success():
    return {"success": True}


@app.route("/api/failure", methods=["GET"])
def failure():
    raise InternalServerError


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
