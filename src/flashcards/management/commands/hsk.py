from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Prints 'Hello World' to the console"

    def add_arguments(self, parser):
        parser.add_argument("--up", action="store_true")
        parser.add_argument("--down", action="store_true")

    def handle(self, *args, **options):
        if options["up"]:
            self.up()
        elif options["down"]:
            self.down()

    def up(self):
        self.stdout.write(self.style.SUCCESS("Hello World, up we go!"))

    def down(self):
        self.stdout.write(self.style.SUCCESS("Hello World, down we go!"))
