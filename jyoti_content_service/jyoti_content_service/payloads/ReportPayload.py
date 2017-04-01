
class ReportPayload:

    def __init__(self, data_source, latitude, longitude, report_type, report_content, name=None, evidence=None):
        self.data_source = data_source
        self.latitude = latitude
        self.longitude = longitude
        self.report_type = report_type
        self.report_content = report_content
        if evidence is not None:
            self.evidence = evidence
        if name is not None:
            self.name = name
