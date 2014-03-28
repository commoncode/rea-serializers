from rest_framework import serializers

from rea.models.contracts import Contract, ContractClause, Clause, ClauseRuleAspect

from cqrs.serializers import CQRSSerializer, CQRSPolymorphicSerializer


class ContractSerializer(CQRSPolymorphicSerializer):
    '''
    Serializer for the `ContractContract` model
    '''
    # order = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Contract
        fields = (
            'id', 'title', 'short_title'
        )


class ClauseSerializer(CQRSSerializer):
    '''
    Serializer for the `Clause` model
    '''
    class Meta:
        model = Clause
        fields = ( 'id', )


class ClauseRuleAspectSerializer(CQRSSerializer):
    '''
    Serializer for the `ClauseRuleAspect` model
    '''
    clause = ClauseSerializer()

    class Meta:
        model = ClauseRuleAspect
        fields = (
            'id', 'created_at', 'created_by', 'modified_at',
            'modified_by', 'clause'
        )


class ContractClauseSerializer(CQRSSerializer):
    '''
    Serializer for the `ContractClause` model
    '''
    contract = ContractSerializer()
    clause = ClauseSerializer()

    class Meta:
        model = ContractClause
        fields = (
            'id', 'contract', 'clause'
        )
