from rea.models.agents import Agent

from cqrs.mongo import CQRSPolymorphicSerializer


class AgentSerializer(CQRSPolymorphicSerializer):
    """
    Serializer for the `SubscriptionContract` model
    """
    class Meta:
        model = Agent
        fields = (
            "id", "title", "short_title"
        )
