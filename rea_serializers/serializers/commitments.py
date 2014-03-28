from rea.models.commitments import (
    Commitment, IncrementCommitment, DecrementCommitment
)

from cqrs.serializers import CQRSSerializer

from .agents import AgentSerializer
from .contracts import ContractSerializer
from .resources import ResourceSerializer


class IncrementCommitmentSerializer(CQRSSerializer):
    """
    Serializer for the `IncrementCommitment` model
    """
    providing_agent = AgentSerializer()
    recieving_agent = AgentSerializer()
    resource = ResourceSerializer()

    class Meta:
        model = IncrementCommitment
        fields = (
            "id", "providing_agent", "recieving_agent", "resource", "quantity"
        )


class DecrementCommitmentSerializer(CQRSSerializer):
    """
    Serializer for the `DecrementCommitment` model
    """
    providing_agent = AgentSerializer()
    recieving_agent = AgentSerializer()
    resource = ResourceSerializer()

    class Meta:
        model = DecrementCommitment
        fields = (
            "id", "providing_agent", "recieving_agent", "resource", "quantity"
        )


class CommitmentSerializer(CQRSSerializer):
    """
    Serializer for the `Commitment` model
    """
    contract = ContractSerializer()

    class Meta:
        model = Commitment
        fields = (
            "id", "occured_at", "contract"
        )
