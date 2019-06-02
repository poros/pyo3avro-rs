from pyo3avro_rs import Schema


def test_dummy() -> None:
    schema = Schema('{"type": "string"}')
    assert schema is not None
