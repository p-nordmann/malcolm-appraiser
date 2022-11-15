"""
We provide basic unit tests here, to be able to have at least some confidence the code works.

TODO much too much...
"""

from concurrent import futures
from unittest import mock

import grpc
import pytest

from malcolm_appraiser import MalcolmSampler
from malcolm_appraiser.malcolms_service_pb2 import (
    UUID,
    Boundaries,
    Samples,
    WalkRequest,
)
from malcolm_appraiser.malcolms_service_pb2_grpc import (
    AppraiserStub,
    add_AppraiserServicer_to_server,
)


@pytest.fixture
def fake_stub():
    """Uses a MagicMock as servicer."""
    return mock.MagicMock()


@pytest.fixture
def mock_appraiser_stub(fake_stub):
    """Patches the AppraiserStub with fake_stub."""
    with mock.patch(
        "malcolm_appraiser.malcolm_sampler.AppraiserStub", lambda *_: fake_stub
    ):
        yield


class TestMalcolmSampler:
    """Test that MalcolmSampler class provides the correct API.

    We mock the grpc service and make sure it performs the correct calls.
    """

    def test_set_boundaries(self, fake_stub, mock_appraiser_stub):
        """set_boundaries should send dimension and boundaries to the server."""
        fake_stub.PutBoundaries.return_value = UUID(uuid="fake_uuid")

        sampler = MalcolmSampler("anything")
        sampler.set_boundaries([[0, 3]] * 3)

        assert fake_stub.PutBoundaries.call_count == 1
        assert fake_stub.RegisterTrueSamples.call_count == 0

        args, kwargs = fake_stub.PutBoundaries.call_args
        assert args == (Boundaries(dimension=3, infima=[0, 0, 0], suprema=[3, 3, 3]),)
        assert kwargs == {}

    def test_set_posterior(self, fake_stub, mock_appraiser_stub):
        """set_posterior should send correct uuid, points and posterior values to the server."""
        fake_stub.PutBoundaries.return_value = UUID(uuid="fake_uuid_0")
        fake_stub.RegisterTrueSamples.return_value = UUID(uuid="fake_uuid_1")

        sampler = MalcolmSampler("anything")
        sampler.set_boundaries([[0, 3]] * 3)
        sampler.set_posterior(
            [[0, 0, 0], [1, 1, 1], [2, 2, 2]],
            [1, 2, 3],
        )

        assert fake_stub.PutBoundaries.call_count == 1
        assert fake_stub.RegisterTrueSamples.call_count == 1

        args, kwargs = fake_stub.RegisterTrueSamples.call_args
        assert len(args) == 1
        assert kwargs == {}

        points, posterior_values = [], []
        for true_sample in args[0]:
            assert true_sample.uuid == "fake_uuid_0"
            for k, posterior_value in enumerate(true_sample.posterior_values):
                points.append(true_sample.coordinates[3 * k : 3 * (k + 1)])
                posterior_values.append(posterior_value)

        assert points == [[0.0, 0.0, 0.0], [1.0, 1.0, 1.0], [2.0, 2.0, 2.0]]
        assert posterior_values == [1.0, 2.0, 3.0]

    @staticmethod
    def validate_boundaries(coordinates, boundaries):
        """Validates that coordinates lie within boundaries."""
        assert len(coordinates) == len(boundaries)
        for x, (inf, sup) in zip(coordinates, boundaries):
            assert inf <= x and x <= sup

    def test_make_samples(self, fake_stub, mock_appraiser_stub):
        """make_samples should send correct request and allow to iterate on generated samples."""
        fake_stub.PutBoundaries.return_value = UUID(uuid="fake_uuid_0")
        fake_stub.RegisterTrueSamples.return_value = UUID(uuid="fake_uuid_1")

        sample_0 = Samples(uuid="fake_uuid_2", coordinates=[1, 2, 3])
        sample_1 = Samples(uuid="fake_uuid_2", coordinates=[0, 0, 0])
        fake_stub.Walk.return_value = iter([sample_0, sample_1] * 5)

        sampler = MalcolmSampler("anything")
        sampler.set_boundaries([[0, 3]] * 3)
        sampler.set_posterior(
            [[0, 0, 0], [1, 1, 1], [2, 2, 2]],
            [1, 2, 3],
        )
        samples = sampler.make_samples(10)

        # Validate call args.
        assert fake_stub.PutBoundaries.call_count == 1
        assert fake_stub.RegisterTrueSamples.call_count == 1
        assert fake_stub.Walk.call_count == 1

        args, kwargs = fake_stub.Walk.call_args
        assert len(args) == 1
        assert kwargs == {}

        assert isinstance(args[0], WalkRequest)
        assert args[0].uuid == "fake_uuid_1"
        self.validate_boundaries(args[0].starting_point, [[0, 3]] * 3)
        assert args[0].number_of_samples == 10

        # Validate return values.
        assert samples == [[1.0, 2.0, 3.0], [0.0, 0.0, 0.0]] * 5
