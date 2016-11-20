import icalendar
from datetime import datetime, timedelta
from dateutil import rrule
import StringIO

def make_15m_recurring_ical(startDateTime):
    ev = icalendar.Event()
    ev.add('summary', "15 Minute Difference")
    ev.add('dtstart', startDateTime)
    ev.add('rrule', {'freq':'weekly'})
    ev.add('dtend', startDateTime + timedelta(minutes=15))

    cal = icalendar.Calendar()
    cal.add_component(ev)
    
    iCalString = cal.to_ical()
    return iCalString

