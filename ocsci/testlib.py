from ocsci.pytest_customization.marks import *  # noqa: F403
from utility import environment_check as ec


@pytest.mark.usefixtures(  # noqa: F405
    ec.environment_checker.__name__,
)
class BaseTest():
    """
    Base test class for our testing.
    If some functionallity/property needs to be implemented in all test classes
    here is the place to put your code.
    """
    pass


@e2e  # noqa: F405
class E2ETest(BaseTest):
    """
    Base class for E2E team
    """
    pass


@manage  # noqa: F405
class ManageTest(BaseTest):
    """
    Base class for E2E team
    """
    pass


@ecosystem  # noqa: F405
class EcosystemTest(BaseTest):
    """
    Base class for E2E team
    """
    pass
