with open("Parole_Input.txt", encoding='ansi', mode="r") as f_in, open("Parole_Output.txt", encoding='ansi', mode="w") as f_out:
  prev_line = None
  for line in f_in:
    if prev_line and line[:3] == prev_line[:3]:
      continue # Ignora la riga corrente se i primi 3 caratteri sono uguali alla riga precedente
    f_out.write(line)
    prev_line = line 
