import xml.etree.ElementTree as ET
import json

tree = ET.parse('OTA_AirSeatMapRS.xml')
root = tree.getroot()
seatMap = root[0][0][1][0][1]
ns = '{http://www.opentravel.org/OTA/2003/05/common/}'
cabinClasses = seatMap.findall(ns+'CabinClass')
seats = []

def xmlToJson():
  for clss in cabinClasses:
    layout = clss.get('Layout')
    rows = clss.findall(ns+'RowInfo')

    for row in rows:
      seatsPerRow = row.findall(ns+'SeatInfo')

      for seat in seatsPerRow:
        _seat = {
          "type": seat.find(ns+'Features').text,
          "id": seat.find(ns+'Summary').get('SeatNumber'),
          "price": "NA",
          "cabin_class": row.get('CabinType'),
          "available": seat.find(ns+'Summary').get('AvailableInd'),
        }
        seats.append(_seat)

  seatsJSON = json.dumps(seats)
  return seatsJSON

xmlToJson()
