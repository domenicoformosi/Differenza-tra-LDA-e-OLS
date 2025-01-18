# App di Confronto tra Regressioni

## Panoramica

Questa applicazione mostra il confronto tra la **Regressione ai Minimi Quadrati Ordinari (OLS)** e la **Regressione ai Minimi Assoluti (LAD)** utilizzando la libreria **Statsmodels** di Python. Viene visualizzato come i due metodi di regressione si comportano su set di dati con e senza outliers, permettendo agli utenti di osservare le differenze nel fitting dei modelli. L'app aiuta a comprendere come gli outliers influenzano i modelli di regressione e perché la **LAD** è più robusta rispetto alla **OLS**.

## Funzionalità principali

- **Visualizzazione Interattiva delle Regressioni**: L'app mostra due tipi di modelli di regressione su due scenari diversi:
  - **Regressione OLS**: Metodo di regressione standard che minimizza la somma dei quadrati dei residui.
  - **Regressione LAD**: Metodo robusto che minimizza la somma dei residui assoluti, rendendolo meno sensibile agli outliers.
  
- **Dati con Outliers**: L'app consente di confrontare visivamente come i modelli di regressione si comportano quando il set di dati contiene outliers. Gli outliers vengono introdotti in posizioni diverse nei dati per simulare irregolarità tipiche nei dati reali.

## Differenze tra OLS e LAD

### OLS (Ordinary Least Squares)

**Pro**:
- **Semplicità e Interpretabilità**: L'OLS è il metodo di regressione più semplice e ben compreso. È facile da implementare e i risultati sono facilmente interpretabili.
- **Efficienza**: Se i dati non contengono outliers, l'OLS è molto efficiente. La stima dei parametri è asintoticamente non distorta e la varianza delle stime è minimizzata.
- **Estrazione di Informazioni Statistiche**: L'OLS fornisce statistiche utili, come il valore di \( R^2 \), i test di significatività dei coefficienti, e intervalli di confidenza per i parametri stimati.

**Contro**:
- **Sensibilità agli Outliers**: L'OLS è molto sensibile agli outliers. Un singolo punto anomalo può influenzare significativamente la retta di regressione, portando a stime distorte dei parametri.
- **Non Robustezza**: Quando i dati non sono distribuiti normalmente o contengono outliers, l'OLS può fornire stime imprecise e fuorvianti.
- **Assunzione di Normalità**: L'OLS presuppone che i residui siano distribuiti normalmente, il che non è sempre il caso nei dati reali.

---

### LAD (Least Absolute Deviations)

**Pro**:
- **Robustezza agli Outliers**: Il principale vantaggio della regressione LAD è la sua robustezza agli outliers. Poiché minimizza la somma dei residui assoluti invece dei quadrati, gli outliers hanno un impatto minimo sui risultati.
- **Adatto per Dati con Distribuzioni Non Normali**: LAD non richiede che i residui siano normalmente distribuiti, rendendolo una scelta migliore quando i dati non soddisfano questa assunzione.
- **Flessibilità**: LAD può essere utilizzato anche in situazioni in cui la relazione tra le variabili non è lineare, sebbene la modellizzazione lineare rimanga una delle sue applicazioni principali.

**Contro**:
- **Minore Efficienza**: Se i dati sono privi di outliers e ben distribuiti, la regressione LAD è meno efficiente dell'OLS. L'OLS fornisce stime più precise in presenza di dati regolari e senza anomalie.
- **Meno Informazioni Statistiche**: La regressione LAD non fornisce statistiche di inferenza come l'OLS (ad esempio, intervalli di confidenza o test t), il che rende più difficile fare inferenze su base statistica.
- **Più Complesso da Interpretare**: I risultati della regressione LAD sono meno facilmente interpretabili rispetto all'OLS, soprattutto quando si cerca di trarre conclusioni sui coefficienti di regressione.

---

### Confronto tra OLS e LAD

| **Caratteristica**        | **OLS**                                     | **LAD**                                      |
|---------------------------|---------------------------------------------|----------------------------------------------|
| **Sensibilità agli Outliers** | Molto sensibile agli outliers.               | Molto robusto agli outliers.                  |
| **Efficienza**             | Alta, quando i dati sono senza outliers.    | Inferiore a OLS in presenza di dati regolari.|
| **Assunzioni**             | Richiede che i residui siano normalmente distribuiti. | Non richiede normalità dei residui.           |
| **Statistiche**            | Fornisce statistiche utili (es. \( R^2 \), test di significatività). | Non fornisce statistiche inferenziali standard. |
| **Interpretabilità**       | Facile da interpretare e spiegare.          | Più difficile da interpretare rispetto a OLS. |

---

### Quando Utilizzare OLS vs LAD

- **Usa OLS**:
  - Quando i dati sono privi di outliers o anomalie.
  - Quando si desidera ottenere stime precise e statistiche inferenziali come i test di significatività.
  - Quando si assume che i residui siano distribuiti normalmente.
  
- **Usa LAD**:
  - Quando i dati contengono outliers o sono influenzati da valori estremi.
  - Quando i dati non seguono una distribuzione normale o hanno una distribuzione pesante di code.
  - Quando si cerca un modello robusto che minimizzi l'impatto di errori anomali nei dati.

---

## Scopo dell'app

L'obiettivo dell'app è di mostrare come le due tecniche di regressione (OLS e LAD) si comportano su dati che includono outliers. Utilizzando due scenari con outliers posizionati in punti diversi dei dati, l'app permette di visualizzare come la regressione OLS venga influenzata negativamente dagli outliers, mentre la regressione LAD rimanga più stabile e robusta.

## Istruzioni per l'installazione

1. **Clona il repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
