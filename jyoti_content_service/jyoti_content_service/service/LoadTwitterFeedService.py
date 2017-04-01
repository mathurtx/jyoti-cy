from local_properties import *
from itertools import islice
from jyoti_content_service.payloads.ReportPayload import ReportPayload
from repository.models import ReportTable

class LoadTwitterFeedService:

    def load_file(self):
        try:
            with open(TWITTER_FILE_PATH, 'rb') as f:
                for n_lines in iter(lambda: tuple(islice(f, BATCH_NUM_LINES)), ()):
                    self.create_payload(n_lines)
        except Exception as e:
            raise e

    def create_payload(self, n_lines):
        payloads = []
        try:
            for line in n_lines:
                column_values = line.split(',')
                if len(column_values) <= 5 and len(column_values) > 7:
                    continue
                report_payload = ReportPayload(column_values[1], column_values[2], column_values[3], column_values[4], column_values[5], evidence=column_values[6], name=column_values[0])
                payloads.append(report_payload)
                ReportTable.objects.bulk_create(payloads)
            return payloads
        except Exception as e:
            raise e
