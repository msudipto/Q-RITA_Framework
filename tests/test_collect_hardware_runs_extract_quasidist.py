import sys
import types
import unittest


if "qiskit_ibm_runtime" not in sys.modules:
    qiskit_ibm_runtime = types.ModuleType("qiskit_ibm_runtime")
    qiskit_ibm_runtime.QiskitRuntimeService = object
    qiskit_ibm_runtime.Sampler = object
    sys.modules["qiskit_ibm_runtime"] = qiskit_ibm_runtime

if "qiskit" not in sys.modules:
    qiskit = types.ModuleType("qiskit")
    qiskit.transpile = lambda *args, **kwargs: None
    sys.modules["qiskit"] = qiskit

import collect_hardware_runs as chruns


class _DummyResult:
    def __init__(self, payload=None, private_result=None):
        self._payload = payload
        self._result = private_result

    def to_dict(self):
        return self._payload


class ExtractQuasidistTests(unittest.TestCase):
    def test_extracts_from_nested_meas_quasi_dists(self):
        res = _DummyResult(
            payload={
                "results": [
                    {"data": {"meas": {"quasi_dists": [{"00": 0.75, "11": 0.25}]}}}
                ]
            }
        )

        self.assertEqual(chruns._extract_quasidist(res), {"00": 0.75, "11": 0.25})

    def test_falls_back_to_private_result_when_nested_shape_missing(self):
        res = _DummyResult(
            payload={"results": [{"data": {"meas": None}}]},
            private_result={"quasi_probabilities": {"01": 1.0}},
        )

        self.assertEqual(chruns._extract_quasidist(res), {"01": 1.0})

    def test_returns_empty_dict_for_malformed_or_missing_data(self):
        res = _DummyResult(payload={"results": [{"data": {"meas": "bad-shape"}}]})

        self.assertEqual(chruns._extract_quasidist(res), {})


if __name__ == "__main__":
    unittest.main()
