# App di Confronto tra Regressioni

## Panoramica

Questa applicazione mostra il confronto tra la **Regressione ai Minimi Quadrati Ordinari (OLS)** e la **Regressione ai Minimi Assoluti (LAD)** utilizzando la libreria **Statsmodels** di Python. Viene visualizzato come i due metodi di regressione si comportano su set di dati con e senza outliers, permettendo agli utenti di osservare le differenze nel fitting dei modelli. L'app aiuta a comprendere come gli outliers influenzano i modelli di regressione e perché la **LAD** è più robusta rispetto alla **OLS**.

> **Nota**: Questa applicazione è stata sviluppata da uno studente di Ingegneria Informatica come progetto personale e non ha alcuna pretesa di essere completamente corretta o priva di errori. L'obiettivo principale è educativo e dimostrativo, e non è garantita l'accuratezza dei risultati o l'adeguatezza a scopi professionali.

## Funzionalità principali

- **Visualizzazione Interattiva delle Regressioni**: L'app mostra due tipi di modelli di regressione su due scenari diversi:
  - **Regressione OLS**: Metodo di regressione standard che minimizza la somma dei quadrati dei residui.
  - **Regressione LAD**: Metodo robusto che minimizza la somma dei residui assoluti, rendendolo meno sensibile agli outliers.
  
- **Dati con Outliers**: L'app consente di confrontare visivamente come i modelli di regressione si comportano quando il set di dati contiene outliers. Gli outliers vengono introdotti in posizioni diverse nei dati per simulare irregolarità tipiche nei dati reali.

## Variabili `outliers1` e `outliers2`

Per personalizzare il numero di outliers nei dati, l'app consente di modificare le variabili `outliers1` e `outliers2`. Queste variabili controllano la **proporzione di outliers** che vengono aggiunti nei due scenari:

- **`outliers1`**: Definisce la proporzione di outliers nel primo scenario. Maggiore è il valore, maggiore sarà la quantità di outliers introdotti nei dati.
- **`outliers2`**: Definisce la proporzione di outliers nel secondo scenario. Anche qui, modificando questo valore, si può variare la quantità di outliers nel secondo set di dati.

### Come Cambiare le Proporzioni degli Outliers

1. **Aumentando `outliers1` o `outliers2`**: Aumentando questi valori, si introduce un numero maggiore di outliers nei dati. Di conseguenza, il modello OLS sarà più influenzato da questi outliers, mentre la regressione LAD sarà meno sensibile e rimarrà più stabile.

2. **Riducendo `outliers1` o `outliers2`**: Riducendo questi valori, si riduce la quantità di outliers nei dati, il che permetterà ai modelli OLS e LAD di comportarsi in modo più simile. Quando i dati sono privi di outliers, l'OLS tende ad essere più efficiente rispetto alla LAD.

### Osservazioni

- **Scenari con pochi outliers**: Quando la proporzione di outliers è bassa, i risultati delle due regressioni saranno simili, ma l'OLS potrebbe essere leggermente più preciso.
- **Scenari con molti outliers**: Quando la proporzione di outliers è alta, la regressione LAD diventa molto utile poiché è meno influenzata da questi valori anomali, mentre l'OLS potrebbe produrre stime distorte.

...

> **Nota Importante**: Eventuali miglioramenti, correzioni o suggerimenti sono benvenuti!

