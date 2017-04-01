TWITTER_FILE_PATH = "/Users/tanmaymathur/Documents/personal_workspace/"
BATCH_NUM_LINES = 100
RADIUS = 5
FIND_ROWS_IN_RADIUS = """SELECT a.latitude, a.longitude, report_type, city
FROM repository_reporttable a
WHERE ("acos(sin(a.latitude * 0.0175) * sin({source_latitude} * 0.0175)+ cos(a.latitude * 0.0175) * cos({source_latitude} * 0.0175)*cos(({source_longitude} * 0.0175) - (a.longitude * 0.0175))) * 3959 <= {radius})"""