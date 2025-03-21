from Events import EventHandler
import datetime

handler = EventHandler()
handler.addEvent("Directory Overflow", datetime.datetime.now(), "High")
handler.checkForEvent()
