from Events import EventHandler
import datetime

handler = EventHandler()
handler.addEvent("Memory Spike", datetime.datetime.now(), "High")
handler.checkForEvent()
