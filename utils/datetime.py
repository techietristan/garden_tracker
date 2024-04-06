from datetime import datetime

def getZFill(format: str) -> str:
    return datetime.now().strftime(format).zfill(2)

def getDateTime() -> str:
    year = datetime.now().strftime('%Y')
    month = getZFill('%m')
    day = getZFill('%d')
    hour = getZFill('%H')
    minute = getZFill('%M')
    second = getZFill('%S')

    return f'{year}-{month}-{day}_{hour}-{minute}-{second}'