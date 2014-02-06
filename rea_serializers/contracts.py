from rest_framework import serializers

from rea.models.contracts import Contract, Clause, ClauseRule, Order

from cqrs.mongo import CQRSSerializer


class OrderSerializer(CQRSSerializer):
    """
    Serializer for the `Order` model
    """
    agent = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Order
        fields = (
            "id", "created_at", "created_by", "agent"
        )


class ContractSerializer(CQRSSerializer):
    """
    Serializer for the `ContractContract` model
    """
    order = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Contract
        fields = (
            "id", "title", "short_title", "order"
        )


class ClauseSerializer(CQRSSerializer):
    """
    Serializer for the `Clause` model
    """
    class Meta:
        model = Clause
        fields = ( "id", )


class ClauseRuleSerializer(CQRSSerializer):
    """
    Serializer for the `ClauseRule` model
    """
    clause = ClauseSerializer()

    class Meta:
        model = ClauseRule
        fields = (
            "id", "created_at", "created_by", "modified_at",
            "modified_by", "clause"
        )


class ContractClauseSerializer(CQRSSerializer):
    """
    Serializer for the `ContractClause` model
    """
    contract = ContractSerializer()
    clause = ClauseSerializer()

    class Meta:
        model = ClauseRule
        fields = (
            "id", "contract", "clause"
        )
