from importlib.metadata import version, PackageNotFoundError
from packaging.version import Version

try:
    elasticsearch_version = Version(version('elasticsearch'))
except PackageNotFoundError:
    elasticsearch_version = Version("0")

print("*"*20, elasticsearch_version)

HAS_ES7 = Version("7") >= elasticsearch_version < Version("8")
HAS_ES8 = Version("8") >= elasticsearch_version < Version("9")
HAS_ES9 = Version("9") >= elasticsearch_version < Version("10")
