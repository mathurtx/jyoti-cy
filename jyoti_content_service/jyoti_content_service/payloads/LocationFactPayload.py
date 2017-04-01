
class LocationFactPayload:

    def __init__(self, latitude, longitude, report_type, report_type_count):
        self.latitude = latitude
        self.longitude = longitude
        self.report_type = report_type
        self.report_type_count = report_type_count