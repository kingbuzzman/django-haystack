import os
import unittest

from django.conf import settings

from haystack.utils import log as logging
from haystack.compat import HAS_ES7


def load_tests(loader, standard_tests, pattern):
    log = logging.getLogger("haystack")
    if not HAS_ES7:
        log.error(
            "Skipping ElasticSearch 7 tests: 'elasticsearch>=7.0.0,<8.0.0' not installed."
        )
        raise unittest.SkipTest("'elasticsearch>=7.0.0,<8.0.0' not installed.")

    from elasticsearch import Elasticsearch, exceptions

    url = settings.HAYSTACK_CONNECTIONS["elasticsearch"]["URL"]
    es = Elasticsearch(url)
    try:
        es.info()
    except exceptions.ConnectionError as e:
        log.error("elasticsearch not running on %r" % url, exc_info=True)
        raise unittest.SkipTest("elasticsearch not running on %r" % url, e)

    package_tests = loader.discover(
        start_dir=os.path.dirname(__file__), pattern=pattern
    )
    standard_tests.addTests(package_tests)
    return standard_tests
