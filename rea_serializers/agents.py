from rea.models.agents import Agent

from cqrs.mongo import CQRSSerializer


class AgentSerializer(CQRSSerializer):
    """
    Serializer for the `SubscriptionContract` model
    """
    class Meta:
        model = Agent
        fields = (
            "id", "title", "short_title"
        )
