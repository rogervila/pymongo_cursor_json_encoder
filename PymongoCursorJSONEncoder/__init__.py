from datetime import datetime, date
from isodate import datetime_isoformat
from bson import ObjectId
from json import JSONEncoder


class MongoJSONEncoder(JSONEncoder):
    def default(self, output):
        if isinstance(output, (datetime, date)):
            return datetime_isoformat(output)

        if isinstance(output, ObjectId):
            return str(output)

        return super().default(output)
