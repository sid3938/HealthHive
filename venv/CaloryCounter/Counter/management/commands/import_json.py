import json
from django.core.management.base import BaseCommand
from Counter.models import FoodItem
from decimal import Decimal, InvalidOperation

class Command(BaseCommand):
    help = 'Import food items from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='The path to the JSON file')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']

        try:
            with open(json_file, 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            self.stderr.write(f"Error reading JSON file: {e}")
            return

        for row in data:
            try:
                # Ensure required fields are present
                name = row.get('name')
                serving_size = row.get('serving_size')

                if not name or not serving_size:
                    raise KeyError("Missing required fields: 'name' or 'serving_size'")

                # Create the FoodItem object
                FoodItem.objects.create(
                    name=name,
                    serving_size=serving_size,
                    calories=self.convert_to_decimal(row.get('calories')),
                    carbohydrate=self.convert_to_decimal(row.get('carbohydrate')),
                    cholesterol=self.convert_to_decimal(row.get('cholesterol')),
                    total_fat=self.convert_to_decimal(row.get('total_fat')),
                    saturated_fat=self.convert_to_decimal(row.get('saturated_fat')),
                    fiber=self.convert_to_decimal(row.get('fiber')),
                    protein=self.convert_to_decimal(row.get('protein')),
                    sodium=self.convert_to_decimal(row.get('sodium')),
                    sugars=self.convert_to_decimal(row.get('sugars'))
                )
                self.stdout.write(self.style.SUCCESS(f"Successfully imported: {name}"))

            except (InvalidOperation, KeyError, ValueError) as e:
                self.stderr.write(f"Error importing item {row.get('name', 'Unknown')}: {e}")
                self.stderr.write(f"Item data: {row}")  # Log the problematic row for debugging

        self.stdout.write(self.style.SUCCESS('Finished importing data from JSON'))

    def convert_to_decimal(self, value):
        """
        Converts a value to Decimal, returning 0.00 for invalid inputs.
        """
        try:
            return Decimal(value)
        except (InvalidOperation, TypeError, ValueError):
            return Decimal('0.00')
