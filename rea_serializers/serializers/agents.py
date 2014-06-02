from rea.models.agents import Agent

from cqrs.serializers import CQRSPolymorphicSerializer


class AgentSerializer(CQRSPolymorphicSerializer):

    class Meta:
        model = Agent
        exclude = 'slug',
