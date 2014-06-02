from rea.models.commitments import (
    Commitment, IncrementCommitment, DecrementCommitment
)

from cqrs.serializers import CQRSPolymorphicSerializer

from .agents import AgentSerializer
from .contracts import ContractSerializer
from .resources import ResourceSerializer


class IncrementCommitmentSerializer(CQRSPolymorphicSerializer):
    providing_agent = AgentSerializer()
    recieving_agent = AgentSerializer()
    resource = ResourceSerializer()

    class Meta:
        model = IncrementCommitment


class DecrementCommitmentSerializer(CQRSPolymorphicSerializer):
    providing_agent = AgentSerializer()
    recieving_agent = AgentSerializer()
    resource = ResourceSerializer()

    class Meta:
        model = DecrementCommitment


class CommitmentSerializer(CQRSPolymorphicSerializer):
    contract = ContractSerializer()

    class Meta:
        model = Commitment
        exclude = 'increment', 'decrement'
