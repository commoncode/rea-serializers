from cqrs.mongo import CQRSSerializer

from rea.models.events import Event, IncrementLine, DecrementLine

from .agents import AgentSerializer
from .resources import ResourceSerializer
from .contracts import ContractSerializer
from .commitments import CommitmentSerializer


class IncrementLineSerializer(CQRSSerializer):
    """
    Serializer for the `IncrementLine` model
    """
    contract = ContractSerializer()
    providing_agent = AgentSerializer()
    recieving_agent = AgentSerializer()
    resource = ResourceSerializer()

    class Meta:
        model = IncrementLine
        fields = (
            "id", "providing_agent", "recieving_agent",
            "resource", "quantity"
        )


class DecrementLineSerializer(CQRSSerializer):
    """
    Serializer for the `DecrementLine` model
    """
    contract = ContractSerializer()
    providing_agent = AgentSerializer()
    recieving_agent = AgentSerializer()
    resource = ResourceSerializer()

    class Meta:
        model = DecrementLine
        fields = (
            "id", "providing_agent", "recieving_agent",
            "resource", "quantity"
        )


class EventSerializer(CQRSSerializer):
    """
    Serializer for the `Event` model
    """
    commitment = CommitmentSerializer()
    increment = IncrementLineSerializer()
    decrement = DecrementLineSerializer()

    class Meta:
        model = Event
        fields = (
            "id", "commitment", "occured_at",
            "increment", "decrement"
        )

