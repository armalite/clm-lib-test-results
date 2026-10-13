### [012 – Jev screening of incoming tool results](experiments/012-jev-result-screening/README.md)

- **Question:** can Jev screen document-search results before they reach Claude, reducing work while keeping answers correct? It was tested on a new 40-document handbook question-answering workload with a deterministic search tool and saved originals.
- **Offline:** the earlier incident traces offered no meaningful opportunity. Ordinary searches on the handbook return mostly same-subject passages (1–2% clearly irrelevant).
- **Component diagnostic** (frozen, 36 labelled results, run once): **58/58** support passages kept, **23/23** complete evidence sets kept, and **22%** of text omitted, so the gate passed. The threshold was set to 0.5 from the development cases; the term-match baseline omits nothing.
- **Development pilot** (2 instances × A/B): all 4 runs correct. But **Claude never called search in the screening condition**: it read the documents directly. So screening was never exercised, and the pilot shows no effect either way.
- **Spend:** USD 0.52.
- **What it means:** a search-result filter only matters when the agent depends on search. On a corpus this small it does not.
