from fern_labour_core.exceptions.application import ApplicationError


def test_can_instantiate_application_error() -> None:
    error = ApplicationError("Test")
    assert isinstance(error, ApplicationError)
