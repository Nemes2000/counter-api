from flask.typing import ResponseReturnValue
from flask_openapi3 import Tag, APIView
from http import HTTPStatus

from models.counter import CounterBody
from models.error import ErrorResponse
from services.counter_service import CounterService


api_view = APIView(url_prefix="/api/v1", view_tags=[Tag(name="counter")])


@api_view.route("/counter")
class CounterController:
    @api_view.doc(  # type: ignore[misc]
        summary="Get counter value.",
        responses={
            HTTPStatus.OK: {"content": {"text/plain": {"schema": {"type": "string"}}}},
            HTTPStatus.INTERNAL_SERVER_ERROR: {
                "content": {
                    "application/json": {"schema": ErrorResponse.model_json_schema()}
                },
            },
        },
    )
    def get(self) -> ResponseReturnValue:
        try:
            print("get")
            res = CounterService.get_counter()
        except Exception as e:
            print(e)
            return (
                ErrorResponse(msg="Failed to get counter value.").model_dump(),
                HTTPStatus.INTERNAL_SERVER_ERROR,
            )
        return CounterBody(value=res).model_dump(), HTTPStatus.OK

    @api_view.doc(  # type: ignore[misc]
        summary="Set counter value to the given number. The value can be only a positive number!",
        responses={
            HTTPStatus.OK: {
                "content": {
                    "application/json": {
                        "schema": {
                            "type": "object",
                            "properties": {"value": {"type": "integer"}},
                        }
                    }
                }
            },
            HTTPStatus.BAD_REQUEST: {
                "content": {
                    "application/json": {"schema": ErrorResponse.model_json_schema()}
                },
            },
            HTTPStatus.INTERNAL_SERVER_ERROR: {
                "content": {
                    "application/json": {"schema": ErrorResponse.model_json_schema()}
                },
            },
        },
    )
    def post(self, body: CounterBody) -> ResponseReturnValue:
        if body.value < 0:
            return (
                ErrorResponse(msg="Value must be a positive number.").model_dump(),
                HTTPStatus.BAD_REQUEST,
            )

        try:
            print(body)
            CounterService.update_counter(body.value)

        except Exception as e:
            print(e)
            return (
                ErrorResponse(msg="Failed to update counter.").model_dump(),
                HTTPStatus.INTERNAL_SERVER_ERROR,
            )
        return "", HTTPStatus.OK

    @api_view.doc(  # type: ignore[misc]
        summary="Reset counter value to 0",
        responses={
            HTTPStatus.NO_CONTENT: {
                "content": {
                    "application/json": {"schema": ErrorResponse.model_json_schema()}
                }
            },
            HTTPStatus.INTERNAL_SERVER_ERROR: {
                "content": {
                    "application/json": {"schema": ErrorResponse.model_json_schema()}
                },
            },
        },
    )
    def delete(self) -> ResponseReturnValue:
        try:
            print("delete")
            CounterService.clear_counter()
        except Exception as e:
            print(e)
            return (
                ErrorResponse(msg="Failed to clear counter value.").model_dump(),
                HTTPStatus.INTERNAL_SERVER_ERROR,
            )
        return "", HTTPStatus.NO_CONTENT
