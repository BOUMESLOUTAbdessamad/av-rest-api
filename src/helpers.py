import dateutil.parser
import babel
from constants import RECORDS_PER_PAGE

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      pattern="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      pattern="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, pattern, locale='en')

def paginate_data(request, data):
    page = request.args.get("page", 1, type=int)

    start = (page - 1) * RECORDS_PER_PAGE
    end = start + RECORDS_PER_PAGE

    data = [hike.format() for hike in data]
    current_data = data[start:end]

    return current_data