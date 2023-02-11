import random
from copy import deepcopy
from typing import Sequence

import grpc

from malcolm_appraiser.malcolms_service_pb2 import (
    Boundaries,
    BoundariesUUID,
    MakeSamplesRequest,
    PosteriorUUID,
    PosteriorValuesBatch,
)
from malcolm_appraiser.malcolms_service_pb2_grpc import MalcolmSamplerStub


class MalcolmSampler:
    """MalcolmSampler provides a wrapper for gRPC calls to malcolm-sampler service."""

    def __init__(self, url: str):
        self.url = url
        self.boundaries = None
        self.boundaries_uuid = None
        self.posterior_uuid = None

    def set_boundaries(self, boundaries: Sequence):
        """Registers boundaries to the grpc service."""
        with grpc.insecure_channel(self.url) as chan:
            uuid = MalcolmSamplerStub(chan).AddBoundaries(
                Boundaries(
                    dimension=len(boundaries),
                    infima=[bounds[0] for bounds in boundaries],
                    suprema=[bounds[1] for bounds in boundaries],
                )
            )
            self.boundaries_uuid = uuid.value
        self.boundaries = deepcopy(boundaries)

    def set_posterior(self, points: Sequence, posterior_values: Sequence):
        """Registers posterior values to the grpc service."""
        with grpc.insecure_channel(self.url) as chan:
            uuid = MalcolmSamplerStub(chan).AddPosterior(
                PosteriorValuesBatch(
                    uuid=BoundariesUUID(value=self.boundaries_uuid),
                    coordinates=point,
                    posterior_values=[posterior_value],
                )
                for point, posterior_value in zip(points, posterior_values)
            )
            self.posterior_uuid = uuid.value

    def make_samples(self, amount: int) -> Sequence:
        """Generates requested amount of samples using the grpc service."""
        dimension = len(self.boundaries)
        origin = [
            random.random() * (bounds[1] - bounds[0]) + bounds[0]
            for bounds in self.boundaries
        ]
        points = []
        with grpc.insecure_channel(self.url) as chan:
            for samples in MalcolmSamplerStub(chan).MakeSamples(
                MakeSamplesRequest(
                    uuid=PosteriorUUID(value=self.posterior_uuid),
                    origin=origin,
                    amount=amount,
                )
            ):
                points.extend(
                    [
                        samples.coordinates[k : k + dimension]
                        for k in range(0, len(samples.coordinates), dimension)
                    ]
                )
        return points
