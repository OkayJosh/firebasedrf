import datetime
from django.utils.timezone import now
from rest_framework import serializers
from django.test import TestCase, override_settings
from phonenumber_field import phonenumber

from .models import OtherFinancials, Income, Expense
from .serializers import OtherFinancialsSerializer, IncomeSerializer, ExpenseSerializer

from rest_framework.viewsets import ModelViewSet
from collections import OrderedDict
from functools import wraps




from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.routers import SimpleRouter
from rest_framework.test import APIRequestFactory

factory = APIRequestFactory()

class IncomeModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Income.objects.create( name ='East-Retail Income', amount='40', comment='from East-Retail')

    def test_name_label(self):
        income = Income.objects.get(id=1)
        field_label = income._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_amount_label(self):
        income=Income.objects.get(id=1)
        field_label = income._meta.get_field('amount').verbose_name
        self.assertEqual(field_label, 'amount')

    def test_name_max_length(self):
        income = Income.objects.get(id=1)
        max_length = income._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_object_name_is_name_comma_amount(self):
        income = Income.objects.get(id=1)
        expected_object_name = f'{income.name}, {income.amount}'
        self.assertEqual(expected_object_name, str(income))

class OtherFinacialsModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        OtherFinancials.objects.create( name ='East-Retail Income', amount='40', comment='from East-Retail')

    def test_name_label(self):
        other = OtherFinancials.objects.get(id=1)
        field_label = other._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_amount_label(self):
        other = OtherFinancials.objects.get(id=1)
        field_label = other._meta.get_field('amount').verbose_name
        self.assertEqual(field_label, 'amount')

    def test_name_max_length(self):
        other = OtherFinancials.objects.get(id=1)
        max_length = other._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_object_name_is_name_comma_amount(self):
        other = OtherFinancials.objects.get(id=1)
        expected_object_name = f'{other.name}, {other.amount}'
        self.assertEqual(expected_object_name, str(other))

class ExpenseModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Expense.objects.create( name ='Cereal', amount='11', comment='11 tons of cereals')

    def test_name_label(self):
        expense = Expense.objects.get(id=1)
        field_label = expense._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_amount_label(self):
        expense = Expense.objects.get(id=1)
        field_label = expense._meta.get_field('amount').verbose_name
        self.assertEqual(field_label, 'amount')

    def test_name_max_length(self):
        expense = Expense.objects.get(id=1)
        max_length = expense._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)

    def test_object_name_is_name_comma_amount(self):
        expense = Expense.objects.get(id=1)
        expected_object_name = f'{expense.name}, {expense.amount}'
        self.assertEqual(expected_object_name, str(expense))

# Serializer Tests
class IncomeSerializerTests(TestCase):
    #Set up non-modified objects used by all test methods
    def setUp(self):
        self.income_attributes = {
            'name': 'East Retail Income',
            'amount':  int(11),
            'comment': 'From East-Retail'
        }

        self.serializer_data = {
            'name': 'East Retail Income',
            'amount': '11',
            'comment': 'From East-Retail'
        }

        self.income = Income.objects.create(**self.income_attributes)
        self.serializer = IncomeSerializer(instance=self.income)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['name', 'amount', 'comment']))

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.income_attributes['name'])

    def test_amount_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['amount'], self.income_attributes['amount'])

    def test_comment_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['comment'], self.income_attributes['comment'])


class ExpenseSerializerTests(TestCase):
    #Set up non-modified objects used by all test methods
    def setUp(self):
        self.expense_attributes = {
            'name': 'East Retail Income',
            'amount': int(11),
            'comment': 'From East-Retail'
        }


        self.serializer_data = {
            'name': 'East Retail Income',
            'amount': '11',
            'comment': 'From East-Retail'
        }


        self.expense = Expense.objects.create(**self.expense_attributes)
        self.serializer = ExpenseSerializer(instance=self.expense)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['name', 'amount', 'comment']))

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.expense_attributes['name'])

    def test_amount_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['amount'], self.expense_attributes['amount'])

    def test_comment_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['comment'], self.expense_attributes['comment'])

class OtherFinancialsSerializerTests(TestCase):
    #Set up non-modified objects used by all test methods
    def setUp(self):
        self.other_attributes = {
            'name': 'East Retail Income',
            'amount': int(11),
            'comment': 'From East-Retail'
        }


        self.serializer_data = {
            'name': 'East Retail Income',
            'amount': '11',
            'comment': 'From East-Retail'
        }


        self.other = OtherFinancials.objects.create(**self.other_attributes)
        self.serializer = OtherFinancialsSerializer(instance=self.other)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['name', 'amount', 'comment']))

    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.other_attributes['name'])

    def test_amount_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['amount'], self.other_attributes['amount'])

    def test_comment_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['comment'], self.other_attributes['comment'])