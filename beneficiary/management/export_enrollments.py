import csv
from django.core.management.base import BaseCommand
from beneficiary.models import Enrollment

class Command(BaseCommand):
    help = 'Export CSV file summary of enrollments'

    def handle(self, *args, **kwargs):
        enrollments = Enrollment.objects.all()

        with open('enrollments.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['enrollment_id', 'household_id', 'household_name', 'household_recipient_full_name', 'cash_offer', 'phone_number'])

            for enrollment in enrollments:
                household = enrollment.household
                recipient = household.person_set.filter(is_recipient=True).first()

                writer.writerow([
                    enrollment.id,
                    household.id,
                    household.name,
                    f'{recipient.first_name} {recipient.last_name}',
                    enrollment.cash_offer,
                    recipient.phone_number
                ])