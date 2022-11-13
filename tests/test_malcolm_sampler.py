"""

"""

import pytest
from malcolm_appraiser import MalcolmSampler


@pytest.fixture(scope="module")
def example_boundaries():
    return [[]]


@pytest.fixture(scope="module")
def example_posterior():
    return [[]], []


@pytest.fixture
def mock_grpc_service():
    ...


@pytest.fixture(scope="module")
def start_grpc_service():
    # TODO setup
    yield
    # TODO cleanup


class TestMalcolmSampler:
    """Test that MalcolmSampler class provides the correct API.

    We mock the grpc service and make sure it performs the correct calls.
    """

    def test_set_boundaries(self, mock_grpc_service, example_boundaries):
        ...

    def test_set_posterior(self, mock_grpc_service, example_posterior):
        ...

    def test_make_samples(self, mock_grpc_service):
        ...


class TestMalcolmSamplerInVivo:
    """End-to-end test for malcolm sampler.

    We provide a malcolm sampler service and test that we get statistically correct results.
    """
