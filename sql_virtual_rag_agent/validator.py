import sqlglot

def validate(sql):
    try:
        parsed = sqlglot.parse_one(sql)

        if parsed.key!="select":
            return False, "Only SELECT allowed"
        
        return True, None
    except Exception as e:
        return False, str(e)