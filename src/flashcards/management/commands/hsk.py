import json
from tqdm import tqdm
from django.core.management.base import BaseCommand
from flashcards.models import FlashcardContent

class Command(BaseCommand):
    help = "Import HSK JSON data into the database"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the JSON file')
        parser.add_argument('hsk_level', type=int, help='HSK level (e.g., 1, 2, 3)')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        hsk_level = kwargs['hsk_level']

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
            return

        for entry in tqdm(data, desc=f"Importing HSK {hsk_level}", unit="card"):
            simplified = entry['simplified']
            radical = entry['radical']
            frequency = entry['frequency']
            pos = entry['pos']

            for form in entry['forms']:
                # Extract data from the forms
                traditional = form['traditional']
                transcriptions = form['transcriptions']
                pinyin = transcriptions['pinyin']
                numeric_pinyin = transcriptions['numeric']
                wade_giles = transcriptions['wadegiles']
                bopomofo = transcriptions['bopomofo']
                romatzyh = transcriptions['romatzyh']
                meanings = form['meanings']
                classifiers = form.get('classifiers', [])

                # Create or update the flashcard content
                FlashcardContent.objects.update_or_create(
                    hsk_level=hsk_level,
                    simplified=simplified,
                    pinyin=pinyin,
                    defaults={
                        'radical': radical,
                        'frequency': frequency,
                        'pos': pos,
                        'traditional': traditional,
                        'numeric_pinyin': numeric_pinyin,
                        'wade_giles': wade_giles,
                        'bopomofo': bopomofo,
                        'romatzyh': romatzyh,
                        'meanings': meanings,
                        'classifiers': classifiers,
                    }
                )

        self.stdout.write(self.style.SUCCESS(f"Successfully imported HSK level {hsk_level} flashcards."))
