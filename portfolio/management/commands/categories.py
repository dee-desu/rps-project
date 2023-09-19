from django.core.management.base import BaseCommand
from portfolio.models import Category


class Command(BaseCommand):
    help = 'Create categories'


    def handle(self, *args, **kwargs):
        arr = ["corporate", "commercial", "entertainment", "f&b"]
        for i in arr:
          Category.objects.create(
          name=i
          
            )
          print("Category created")
          