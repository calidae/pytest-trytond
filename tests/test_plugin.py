import pytest

from trytond.pool import Pool
from trytond.tests.test_tryton import with_transaction


@with_transaction()
@pytest.mark.usefixtures('activate_module')
def test_transaction_decorator():
    assert Pool().get('test.model')


@pytest.mark.usefixtures('transaction')
def test_transaction_fixture_used():
    assert Pool().get('test.model')


def test_transaction_fixture_requested(transaction):
    assert Pool().get('test.model')
