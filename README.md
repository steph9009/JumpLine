# 🚀 JumpLine
###### Script Python per Filtrare Righe Basato sui Primi 3 Caratteri

Questo repository contiene un semplice script Python progettato per leggere un file di testo (`Parole_Input.txt`), filtrare le righe consecutive i cui primi tre caratteri sono identici, e scrivere le righe rimanenti in un nuovo file (`Parole_Output.txt`).

## Funzionamento

Lo script opera nel seguente modo:

1.  **Apre i File**: Apre il file `Parole_Input.txt` in modalità lettura (`r`) e il file `Parole_Output.txt` in modalità scrittura (`w`). Se `Parole_Output.txt` esiste già, verrà sovrascritto. Entrambi i file vengono aperti utilizzando la codifica `ansi`.
2.  **Itera sulle Righe**: Legge il file di input riga per riga.
3.  **Confronta i Primi 3 Caratteri**: Mantiene in memoria la riga precedente che è stata scritta nel file di output. Per ogni nuova riga letta, confronta i suoi primi tre caratteri (`riga[:3]`) con i primi tre caratteri della riga precedente memorizzata (`riga_precedente[:3]`).
4.  **Filtra le Righe**:
    * Se i primi tre caratteri della riga corrente sono **identici** a quelli della riga precedente memorizzata, la riga corrente viene **ignorata** (non viene scritta nel file di output).
    * Se i primi tre caratteri sono **diversi**, o se si tratta della **prima riga** del file, la riga corrente viene **scritta** nel file `Parole_Output.txt` e diventa la nuova "riga precedente memorizzata" per il confronto successivo.
5.  **Chiude i File**: Una volta processate tutte le righe, i file vengono chiusi automaticamente grazie all'uso dell'istruzione `with`.

## Requisiti

* Python 3 installato sul tuo sistema.

## Utilizzo

1.  **Clona o Scarica**: Scarica lo script Python (ad esempio, salvalo come `filtra_parole.py`) e assicurati che si trovi nella stessa directory dei tuoi file di input/output.
2.  **Prepara il File di Input**: Crea un file di testo chiamato `Parole_Input.txt` nella stessa directory. Inserisci il testo che desideri processare, con ogni elemento su una nuova riga. **Importante**: Assicurati che questo file sia salvato con codifica `ansi`.
3.  **Esegui lo Script**: Apri un terminale o prompt dei comandi, naviga nella directory dove hai salvato i file ed esegui lo script con il comando:
    ```bash
    python filtra_parole.py
    ```
    *(Sostituisci `filtra_parole.py` con il nome effettivo che hai dato allo script)*
4.  **Controlla l'Output**: Al termine dell'esecuzione, troverai un nuovo file chiamato `Parole_Output.txt` nella stessa directory. Questo file conterrà le righe del file di input, filtrate secondo la logica descritta.

## Nota sulla Codifica

Lo script utilizza specificamente la codifica `ansi`. Questo potrebbe causare problemi su sistemi non Windows o con caratteri non standard per quella codifica. Se incontri problemi di codifica o preferisci una codifica più universale, puoi modificare le righe `open(...)` nello script per usare `utf-8`:

```python
with open("Parole_Input.txt", encoding='utf-8', mode="r") as f_in, \
     open("Parole_Output.txt", encoding='utf-8', mode="w") as f_out:
    # ... resto dello script ...
```

---

## README - English 🇬🇧

# 🚀 JumpLine
###### Python Script to Filter Lines Based on First 3 Characters

This repository contains a simple Python script designed to read a text file (`Parole_Input.txt`), filter out consecutive lines where the first three characters are identical, and write the remaining lines to a new file (`Parole_Output.txt`).

## How it Works

The script operates as follows:

1.  **Opens Files**: It opens the input file `Parole_Input.txt` in read mode (`r`) and the output file `Parole_Output.txt` in write mode (`w`). If `Parole_Output.txt` already exists, it will be overwritten. Both files are opened using `ansi` encoding.
2.  **Iterates Through Lines**: It reads the input file line by line.
3.  **Compares First 3 Characters**: It keeps track of the previously processed line that was written to the output file. For each new line read, it compares its first three characters (`line[:3]`) with the first three characters of the previously stored line (`prev_line[:3]`).
4.  **Filters Lines**:
    * If the first three characters of the current line are **identical** to those of the previously stored line, the current line is **skipped** (it is not written to the output file).
    * If the first three characters are **different**, or if it's the **first line** of the file, the current line is **written** to `Parole_Output.txt` and becomes the new "previously stored line" for the next comparison.
5.  **Closes Files**: Once all lines have been processed, the files are automatically closed thanks to the `with` statement.

## Requirements

* Python 3 installed on your system.

## Usage

1.  **Clone or Download**: Download the Python script (e.g., save it as `filter_words.py`) and ensure it's in the same directory as your input/output files.
2.  **Prepare Input File**: Create a text file named `Parole_Input.txt` in the same directory. Populate this file with the text you want to process, with each item on a new line. **Important**: Make sure this file is saved with `ansi` encoding.
3.  **Run the Script**: Open a terminal or command prompt, navigate to the directory where you saved the files, and run the script using the command:
    ```bash
    python filter_words.py
    ```
    *(Replace `filter_words.py` with the actual name you gave the script)*
4.  **Check Output**: After the script finishes execution, you will find a new file named `Parole_Output.txt` in the same directory. This file will contain the lines from the input file, filtered according to the described logic.

## Encoding Note

The script specifically uses `ansi` encoding. This might cause issues on non-Windows systems or with characters not standard to that encoding. If you encounter encoding problems or prefer a more universal encoding, you can modify the `open(...)` lines in the script to use `utf-8`:

```python
with open("Parole_Input.txt", encoding='utf-8', mode="r") as f_in, \
     open("Parole_Output.txt", encoding='utf-8', mode="w") as f_out:
    # ... rest of the script ...
