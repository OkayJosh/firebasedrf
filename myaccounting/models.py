from firebase_orm import models

class Expense(models.Model):
    name = models.Field()
    amount = models.Field()
    comment = models.TextField()

    class Meta:
        db_table = 'expense'

    def __str__(self):
        return f'{self.name}, {self.amount}'

class Income(models.Model):
    name = models.Field()
    amount = models.Field()
    comment = models.TextField()  

    class Meta:
        db_table = 'income'

    def __str__(self):
        return f'{self.name}, {self.amount}'  

class OtherFinancials(models.Model):
    name = models.Field()
    amount = models.Field()
    comment = models.TextField()  

    class Meta:
        db_table = 'others'

    def __str__(self):
        return f'{self.name}, {self.amount}'  