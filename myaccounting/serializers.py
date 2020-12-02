from rest_framework import serializers

from .models import Income, Expense, OtherFinancials

class IncomeSerializer(serializers.Serializer):
    name = serializers.CharField()
    amount = serializers.IntegerField()
    comment = serializers.CharField()

    def create(self, validated_data):
        return Income(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()
        return instance

class ExpenseSerializer(serializers.Serializer):
    name = serializers.CharField()
    amount = serializers.IntegerField()
    comment = serializers.CharField()

    def create(self, validated_data):
        return Expense(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()
        return instance

class OtherFinancialsSerializer(serializers.Serializer):
    name = serializers.CharField()
    amount = serializers.IntegerField()
    comment = serializers.CharField()

    def create(self, validated_data):
        return OtherFinancials(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()
        return instance