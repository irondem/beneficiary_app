import csv
from django.core.management.base import BaseCommand
from beneficiary.models import Enrollment


class Command(BaseCommand):
    help = 'Export enrollment summary as CSV'

    def handle(self, *args, **options):
        enrollments = Enrollment.objects.all()

        with open('enrollment_summary.csv', 'w', newline='') as csvfile:
            fieldnames = [
                'enrollment_id',
                'household_id',
                'household_name',
                'household_recipient_full_name',
                'cash_offer',
                'phone_number'
            ]

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for enrollment in enrollments:
                
                recipient = enrollment.household.person_set.filter(is_recipient=True).first()
                full_name = f'{recipient.first_name} {recipient.last_name}' if recipient else ''
            

                writer.writerow({
                    'enrollment_id': enrollment.id,
                    'household_id': enrollment.household_id,
                    'household_name': enrollment.household.name,
                    'household_recipient_full_name':full_name,
                    'cash_offer': enrollment.cash_offer,
                    'phone_number':recipient.phone_number if recipient else ''
                    
                })

        self.stdout.write(self.style.SUCCESS('Enrollment summary exported successfully.'))


