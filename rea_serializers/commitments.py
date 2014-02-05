from rea.models.commitments import (
    Commitment, IncrementCommitment, DecrementCommitment
)

from .agents import AgentSerializer
from .contracts import ContractSerializer
from .core import REASerializer
from .resources import ResourceSerializer


class IncrementCommitmentSerializer(REASerializer):
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


class DecrementCommitmentSerializer(REASerializer):
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


class CommitmentSerializer(REASerializer):
    """
    Serializer for the `Commitment` model
    """
    contract = ContractSerializer()

    class Meta:
        model = Commitment
        fields = (
            "id", "occured_at", "contract"
        )
