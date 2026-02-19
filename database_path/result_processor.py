import decimal, datetime

def process_rows(columns, rows):
    processed = []
    for row in rows:
        item = {}
        for col, val in zip(columns, row):
            if isinstance(val, decimal.Decimal):
                item[col] = float(val)
            elif isinstance(val, datetime.datetime):
                item[col] = val.isoformat()
            else:
                item[col] = val
        processed.append(item)
    return processed