from django.contrib.contenttypes.models import ContentType


def get_content_type(app, label):
    return ContentType.objects.get(app_label=app, model=label)


def get_result_with_contacts_and_emails(offices, contacts, mails):
    for office in offices:
        for phone in contacts:
            if office['id'] == phone['entity_object_id']:
                if 'contacts' in office:
                    office['contacts'].append(phone.copy())
                else:
                    office['contacts'] = [phone]

        for mail in mails:
            if office['organization_id'] == mail['organization_id'] and office['country_id'] == mail['country_id']:
                if 'mails' in office:
                    office['mails'].append(mail.copy())
                else:
                    office['mails'] = [mail]

    return offices
