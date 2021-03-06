"""Tests for the extension system."""

from fava.core import FavaLedger
from .conftest import data_file


def test_report_page_globals():
    """Extensions can register reports."""
    extension_report_ledger = FavaLedger(
        data_file("extension-report-example.beancount")
    )
    result = extension_report_ledger.extensions.reports
    assert result == [("PortfolioList", "Portfolio List")]
