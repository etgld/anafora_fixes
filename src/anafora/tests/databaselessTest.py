# from django.test.simple import DjangoTestSuiteRunner
from django.utils.timezone import override
from django.test.runner import DiscoverRunner


class DatabaselessTestRunner(DiscoverRunner):
    """A test suite runner that does not set up and tear down a database."""

    @override
    def setup_databases(self):
        """Overrides DiscoverRunner"""
        pass

    @override
    def teardown_databases(self, *args):
        """Overrides DiscoverRunner"""
        pass
