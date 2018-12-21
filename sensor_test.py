from sense_hat import SenseHat
sense = SenseHat()

# Define the colours red and green
red = (255, 0, 0)
green = (0, 255, 0)

while True:

  # Take readings from all three sensors
  t = sense.get_temperature()
  p = sense.get_pressure()
  h = sense.get_humidity()

  # Round the values to one decimal place
  t = round(t, 1)
  p = round(p, 1)
  h = round(h, 1)
  
  # Create the message
  # str() converts the value to a string so it can be concatenated
  message = "Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)
  
  if t > 18.3 and t < 26.7:
    bg = green
  else:
    bg = red
  
  # Display the scrolling message
#  sense.show_message(message, scroll_speed=0.05, back_colour=bg)

  acceleration = sense.get_accelerometer_raw()
  x = acceleration['x']
  y = acceleration['y']
  z = acceleration['z']

  x=round(x, 0)
  y=round(y, 0)
  z=round(z, 0)

  print("x={0}, y={1}, z={2}, t={3}, p={4}, h={5}".format(x, y, z, t, p, h))
