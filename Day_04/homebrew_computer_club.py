def dompier_music(switches):
  notes = {
    261: "C4",
    294: "D4",
    329: "E4",
    349: "F4",
    392: "G4",
    440: "A4",
    494: "B4",
    523: "C5",
    0:   "REST",
  }

  out = []
  for value in switches:
    freq = int(value, 2)
    out.append(notes.get(freq, "REST"))
    
  return out
