from rea.models.contracts import Contract, ContractClause, Clause, ClauseRuleAspect

from cqrs.serializers import CQRSPolymorphicSerializer


class ContractSerializer(CQRSPolymorphicSerializer):

    class Meta:
        model = Contract


class ClauseSerializer(CQRSPolymorphicSerializer):

    class Meta:
        model = Clause


class ClauseRuleAspectSerializer(CQRSPolymorphicSerializer):
    clause = ClauseSerializer()

    class Meta:
        model = ClauseRuleAspect


class ContractClauseSerializer(CQRSPolymorphicSerializer):
    contract = ContractSerializer()
    clause = ClauseSerializer()

    class Meta:
        model = ContractClause
