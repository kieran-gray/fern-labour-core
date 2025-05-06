import pytest

from fern_labour_core.exceptions.domain import DomainError
from tests.conftest import SampleEntity, SingleFieldValueObject


def test_entity_id_invariance(sample_entity: SampleEntity) -> None:
    with pytest.raises(DomainError):
        sample_entity.id_ = SingleFieldValueObject(value=123)


def test_entity_equality(
    sample_entity: SampleEntity, single_field_value_object: SingleFieldValueObject
) -> None:
    same_entity = SampleEntity(id_=single_field_value_object, name="abcdef")
    assert sample_entity == same_entity


def test_entity_hash(
    sample_entity: SampleEntity,
    single_field_value_object: SingleFieldValueObject,
    other_single_field_value_object: SingleFieldValueObject,
) -> None:
    same_entity = SampleEntity(id_=single_field_value_object, name="abcdef")
    assert hash(sample_entity) == hash(same_entity)

    different_entity = SampleEntity(id_=other_single_field_value_object, name="abcdef")
    assert hash(sample_entity) != hash(different_entity)
