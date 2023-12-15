def build_from_record(Class, record):
    if not record: return None

    attr = dict(zip(Class.attributes, record))
    obj = Class()
    obj.__dict__ = attr
    return obj

def build_from_records(Class, records):
    return [build_from_record(Class, record) for record in records]