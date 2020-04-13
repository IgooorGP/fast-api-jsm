from django.db import models


class BookStore(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(blank=False, null=False, max_length=200)
    cnpj = models.CharField(blank=False, null=False, max_length=30)

    def __str__(self):
        return self.name


class Book(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(blank=False, null=False, max_length=200)
    qtd = models.IntegerField(default=0)

    book_store = models.ForeignKey(BookStore, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
