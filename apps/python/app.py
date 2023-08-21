import json
import pathlib
from flask import Flask, request
from werkzeug.exceptions import InternalServerError

app = Flask("test_app")

HERE = pathlib.Path(__file__).parent.absolute()

with (HERE / "secret.json").open() as fd:
    SECRET_DATA = json.load(fd)


ACCESS_TOKEN = SECRET_DATA["access_token"]


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
    if "Authorization" in request.headers and request.headers["Authorization"] == f"Bearer {ACCESS_TOKEN}":
        return {"success": True}
    return {"detail": "Unauthorized"}, 401


@app.route("/api/failure", methods=["GET"])
def failure():
    raise InternalServerError


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
