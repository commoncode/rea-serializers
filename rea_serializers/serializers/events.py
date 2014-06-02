from cqrs.serializers import CQRSPolymorphicSerializer

from rea.models.events import Event, IncrementLine, DecrementLine

from .agents import AgentSerializer
from .resources import ResourceSerializer
from .contracts import ContractSerializer
from .commitments import CommitmentSerializer


class IncrementLineSerializer(CQRSPolymorphicSerializer):
    contract = ContractSerializer()
    providing_agent = AgentSerializer()
    recieving_agent = AgentSerializer()
    resource = ResourceSerializer()

    class Meta:
        model = IncrementLine


class DecrementLineSerializer(CQRSPolymorphicSerializer):
    contract = ContractSerializer()
    providing_agent = AgentSerializer()
    recieving_agent = AgentSerializer()
    resource = ResourceSerializer()

    class Meta:
        model = DecrementLine


class EventSerializer(CQRSPolymorphicSerializer):
    commitment = CommitmentSerializer()
    increment = IncrementLineSerializer()
    decrement = DecrementLineSerializer()

    class Meta:
        model = Event
