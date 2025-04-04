from Events import EventHandler
import datetime

handler = EventHandler()
handler.addEvent("Database Error", datetime.datetime.now(), "High")
handler.checkForEvent()
