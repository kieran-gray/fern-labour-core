from fern_labour_core.exceptions.domain import DomainError, DomainValidationError


def test_can_instantiate_domain_error() -> None:
    error = DomainError("Test")
    assert isinstance(error, DomainError)


def test_can_instantiate_domain_validation_error() -> None:
    error = DomainValidationError("Test")
    assert isinstance(error, DomainValidationError)
