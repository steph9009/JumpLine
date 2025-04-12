import argparse
import sys

def filter_lines(input_path, output_path, encoding, chars_to_compare, strip_whitespace, verbose):
    """
    Legge un file di input riga per riga, filtra le righe consecutive
    i cui primi N caratteri sono identici, e scrive le righe rimanenti
    su un file di output.

    Args:
        input_path (str): Percorso del file di input.
        output_path (str): Percorso del file di output.
        encoding (str): Codifica da usare per leggere e scrivere i file.
        chars_to_compare (int): Numero di caratteri iniziali da confrontare.
        strip_whitespace (bool): Se True, rimuove spazi bianchi iniziali/finali
                                 prima del confronto dei caratteri.
        verbose (bool): Se True, stampa messaggi di stato e riepilogo.
    """
    prev_line_prefix = None
    lines_read = 0
    lines_written = 0
    lines_skipped = 0

    if verbose:
        print(f"[*] Avvio elaborazione...", file=sys.stderr)
        print(f"    File Input: {input_path}", file=sys.stderr)
        print(f"    File Output: {output_path}", file=sys.stderr)
        print(f"    Encoding: {encoding}", file=sys.stderr)
        print(f"    Caratteri da confrontare: {chars_to_compare}", file=sys.stderr)
        print(f"    Rimuovi spazi bianchi: {'Sì' if strip_whitespace else 'No'}", file=sys.stderr)

    try:
        with open(input_path, encoding=encoding, mode="r") as f_in, \
             open(output_path, encoding=encoding, mode="w") as f_out:

            for line in f_in:
                lines_read += 1
                current_line_to_compare = line

                # Opzionalmente rimuove spazi bianchi prima del confronto
                if strip_whitespace:
                    current_line_to_compare = line.strip()

                # Estrai il prefisso della riga corrente per il confronto
                # Gestisce anche righe più corte del numero di caratteri richiesto
                current_prefix = current_line_to_compare[:chars_to_compare]

                # Confronta con il prefisso precedente (se esiste)
                if prev_line_prefix is not None and current_prefix == prev_line_prefix:
                    lines_skipped += 1
                    if verbose and lines_skipped % 100 == 0: # Feedback ogni 100 righe saltate
                         print(f"\r[*] Righe saltate: {lines_skipped}...", end="", file=sys.stderr)
                    continue  # Ignora la riga corrente

                # Se non è stata saltata, scrivi la riga ORIGINALE e aggiorna il prefisso precedente
                f_out.write(line)
                lines_written += 1
                prev_line_prefix = current_prefix # Aggiorna con l'ultimo prefisso valido scritto

    except FileNotFoundError:
        print(f"[ERRORE] File di input non trovato: {input_path}", file=sys.stderr)
        sys.exit(1) # Esce con codice di errore
    except IOError as e:
        print(f"[ERRORE] Errore di I/O durante l'accesso ai file: {e}", file=sys.stderr)
        sys.exit(1)
    except UnicodeDecodeError as e:
        print(f"[ERRORE] Errore di decodifica nel file di input con encoding '{encoding}': {e}", file=sys.stderr)
        print(f"[*] Suggerimento: Prova a specificare l'encoding corretto con l'opzione --encoding.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"[ERRORE] Errore inaspettato: {e}", file=sys.stderr)
        sys.exit(1)

    if verbose:
        # Assicura che l'eventuale output parziale di righe saltate venga sovrascritto
        print(f"\r[*] Elaborazione completata.", file=sys.stderr)
        print(f"    Righe lette: {lines_read}", file=sys.stderr)
        print(f"    Righe scritte: {lines_written}", file=sys.stderr)
        print(f"    Righe saltate: {lines_skipped}", file=sys.stderr)
    elif lines_skipped > 0 : # Stampa comunque un minimo di info se qualcosa è stato saltato
         print(f"Righe saltate: {lines_skipped}", file=sys.stderr)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Filtra un file di testo rimuovendo le righe consecutive i cui primi N caratteri sono uguali."
    )

    # Argomenti Posizionali (Obbligatori)
    parser.add_argument("input_file", help="Percorso del file di testo di input.")
    parser.add_argument("output_file", help="Percorso del file di testo di output.")

    # Argomenti Opzionali
    parser.add_argument(
        "-c", "--chars",
        type=int,
        default=3,
        help="Numero di caratteri iniziali da confrontare (default: 3)."
    )
    parser.add_argument(
        "-e", "--encoding",
        type=str,
        default="utf-8",
        help="Codifica dei file di input e output (default: utf-8). Prova 'ansi', 'latin-1', 'cp1252' se hai problemi."
    )
    parser.add_argument(
        "-s", "--strip",
        action="store_true", # Se presente, imposta a True
        help="Rimuovi spazi bianchi iniziali/finali dalle righe PRIMA di confrontare i caratteri."
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Stampa informazioni dettagliate durante l'esecuzione."
    )

    args = parser.parse_args()

    # Verifica che il numero di caratteri sia valido
    if args.chars < 0:
        print("[ERRORE] Il numero di caratteri da confrontare non può essere negativo.", file=sys.stderr)
        sys.exit(1)

    # Chiama la funzione principale con gli argomenti parsati
    filter_lines(
        input_path=args.input_file,
        output_path=args.output_file,
        encoding=args.encoding,
        chars_to_compare=args.chars,
        strip_whitespace=args.strip,
        verbose=args.verbose
    )
