from haystack.backends.elasticsearch_backend import (
    ElasticsearchSearchBackend,
    ElasticsearchSearchQuery,
    ElasticsearchSearchEngine,
)
from haystack.exceptions import MissingDependency
from haystack.compat import HAS_ES7

if not HAS_ES7:
    raise MissingDependency(
        "The 'elasticsearch7' backend requires the \
                            installation of 'elasticsearch>=7.0.0,<8.0.0'. \
                            Please refer to the documentation."
    )

Elasticsearch7SearchBackend = ElasticsearchSearchBackend
Elasticsearch7SearchQuery = ElasticsearchSearchQuery
Elasticsearch7SearchEngine = ElasticsearchSearchEngine
