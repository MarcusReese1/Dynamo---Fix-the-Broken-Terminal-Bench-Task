import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")


def load_report():
    assert REPORT_PATH.is_file(), "/app/report.json was not produced"

    try:
        return json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise AssertionError("/app/report.json is not valid JSON") from exc


def test_report_is_json_object_with_exact_keys():
    """Success criterion 1: the report is a JSON object with exactly the required keys."""
    report = load_report()

    assert isinstance(report, dict), "report must be a JSON object"
    assert set(report) == {
        "total_requests",
        "unique_ips",
        "top_path",
    }


def test_request_and_unique_ip_counts():
    """Success criterion 2: request and distinct-client counts are correct."""
    report = load_report()

    assert report["total_requests"] == 6
    assert report["unique_ips"] == 3


def test_top_path():
    """Success criterion 3: top_path is the most frequently requested path."""
    report = load_report()

    assert report["top_path"] == "/index.html"