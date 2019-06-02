import pytest
from pyo3avro_rs import Schema


def test_dummy() -> None:
    assert Schema('{"type": "string"}')


def test_wrong_schema() -> None:
    # should be ValueError, see https://github.com/PyO3/pyo3/issues/488
    with pytest.raises(SystemError):
        Schema('{"type": "error"}')
