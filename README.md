# 🚀 JumpLine 🇮🇹

##### Script per pulire righe consecutive basato sui primi N caratteri

**(Script aggiornato al: 12 aprile 2025)**

## A Cosa Serve?

Questo script "pulisce" un file di testo. Rimuove le righe che iniziano nello stesso modo della riga immediatamente precedente (che è stata tenuta).

È utile per sfoltire elenchi o file dove ci sono molte righe consecutive che differiscono solo verso la fine, rendendo il file più corto e meno ripetitivo.

**Esempio:** Se controlla i primi 3 caratteri:

*Input:*
```plaintext
Apple Pie
Apple Tart
Apple Crumble
Banana Bread
Banana Split
Cherry Pie
```

*Output:*
```plaintext
Apple Pie
Banana Bread
Cherry Pie
```
(Perché "App" era uguale, "App" era uguale, poi "Ban" era diverso, "Ban" era uguale, poi "Che" era diverso).

## Come Funziona?

Lo script legge il tuo file riga per riga e confronta l'inizio di ogni riga con l'inizio dell'ultima riga che ha deciso di *tenere*.

* Se l'inizio è **diverso**, tiene la riga corrente.
* Se l'inizio è **uguale**, butta via la riga corrente.

Per impostazione predefinita, controlla i primi **3** caratteri, ma puoi cambiare questo numero. Puoi anche dirgli di ignorare spazi bianchi all'inizio o alla fine delle righe prima di fare il confronto.

## Come si Usa?

1.  Assicurati di avere **Python 3** installato.
2.  Salva lo script con un nome (es. `pulisci_righe.py`).
3.  Apri un terminale o prompt dei comandi.
4.  Esegui il comando:

    ```bash
    python pulisci_righe.py file_input.txt file_output.txt [opzioni]
    ```

    * Sostituisci `file_input.txt` con il nome del tuo file da pulire.
    * Sostituisci `file_output.txt` con il nome che vuoi dare al file pulito (verrà creato o sovrascritto).

### Personalizzare il Comportamento (Opzioni Comuni)

* **Cambiare quanti caratteri controllare:**
    Usa `-c` seguito da un numero (o `--chars` seguito da un numero).
    *Esempio per controllare i primi 5 caratteri:*
    ```bash
    python pulisci_righe.py input.txt output.txt -c 5
    ```

* **Ignorare spazi inizio/fine riga:**
    Aggiungi l'opzione `-s` (o `--strip`). Utile se le righe hanno indentature diverse.
    *Esempio:*
    ```bash
    python pulisci_righe.py input_con_spazi.txt output.txt -s
    ```

* **Se il file ha problemi di caratteri (encoding):**
    Di solito funziona, ma se vedi caratteri strani, potresti dover specificare la codifica giusta con `-e` (o `--encoding`).
    *Esempio per file vecchi Windows (ANSI):*
    ```bash
    python pulisci_righe.py vecchio_file.txt output.txt -e cp1252
    ```

* **Vedere tutte le opzioni:**
    ```bash
    python pulisci_righe.py --help
    ```

---

# 🚀 JumpLine 🇬🇧

##### Clean Consecutive Lines Script

**(Script updated: April 12, 2025)**

## What Does It Do?

This script "cleans" a text file. It removes lines that start the same way as the previous line that was kept.

It's useful for tidying up lists or files where you have many consecutive lines that only differ towards the end, making the file shorter and less repetitive.

**Example:** If checking the first 3 characters:

*Input:*
```plaintext
Apple Pie
Apple Tart
Apple Crumble
Banana Bread
Banana Split
Cherry Pie
```

*Output:*
```plaintext
Apple Pie
Banana Bread
Cherry Pie
```
(Because "App" was the same, "App" was the same, then "Ban" was different, "Ban" was the same, then "Che" was different).

## How Does It Work?

The script reads your file line by line and compares the beginning of each line with the beginning of the last line it decided to *keep*.

* If the start is **different**, it keeps the current line.
* If the start is **the same**, it throws away the current line.

By default, it checks the first **3** characters, but you can change this number. You can also tell it to ignore whitespace (spaces, tabs) at the beginning or end of lines before comparing.

## How to Use It?

1.  Make sure you have **Python 3** installed.
2.  Save the script with a name (e.g., `clean_lines.py`).
3.  Open a terminal or command prompt.
4.  Run the command:

    ```bash
    python clean_lines.py input_file.txt output_file.txt [options]
    ```

    * Replace `input_file.txt` with the name of your file to clean.
    * Replace `output_file.txt` with the name you want for the clean result file (it will be created or overwritten).

### Customizing How It Works (Common Options)

* **Change how many characters to check:**
    Use `-c` followed by a number (or `--chars` followed by a number).
    *Example to check the first 5 characters:*
    ```bash
    python clean_lines.py input.txt output.txt -c 5
    ```

* **Ignore spaces at the start/end of lines:**
    Add the `-s` option (or `--strip`). Useful if lines have different indentation.
    *Example:*
    ```bash
    python clean_lines.py input_with_spaces.txt output.txt -s
    ```

* **If the file has character problems (encoding):**
    It usually works, but if you see weird characters, you might need to specify the correct encoding with `-e` (or `--encoding`).
    *Example for older Windows (ANSI) files:*
    ```bash
    python clean_lines.py old_file.txt output.txt -e cp1252
    ```

* **See all options:**
    ```bash
    python clean_lines.py --help
    ```
