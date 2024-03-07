from django.db import models

# Create your models here.


class Function(models.Model):
    HARDCOVER = 1
    PAPERBACK = 2
    EBOOK = 3
    BOOK_TYPES = (
        (HARDCOVER, 'Hardcover'),
        (PAPERBACK, 'Paperback'),
        (EBOOK, 'E-functiontion'),
    )
    title = models.CharField(max_length=50)
    publication_date = models.DateField(null=True)
    function_type = models.PositiveSmallIntegerField(choices=BOOK_TYPES)
