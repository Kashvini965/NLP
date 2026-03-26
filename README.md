# NLP Lab Experiments (Ex 1–12)

Python implementations of all 12 NLP lab exercises from the record.

## Experiments

| File | Experiment |
|------|-----------|
| `ex01_basic_text_processing.py` | Basic Text Processing (tokenization, stemming, lemmatization) |
| `ex02_ngram_language_model.py` | N-Gram Language Model |
| `ex03_feature_extraction.py` | Feature Extraction – BoW & TF-IDF |
| `ex04_word2vec_embedding.py` | Word Embedding using Word2Vec |
| `ex05_mimo_hyperparameter.py` | MIMO Neural Network with Keras Tuner |
| `ex06_text_classification_nb_svm.py` | Text Classification – Naïve Bayes & SVM |
| `ex07_kmeans_clustering.py` | K-Means Clustering on Text Data |
| `ex08_pos_tagging.py` | Part-of-Speech (POS) Tagging |
| `ex09_neural_network_text.py` | Text Classification with Neural Network |
| `ex10_lstm_text_processing.py` | Next-Word Prediction with LSTM |
| `ex11_hmm_crf_sequence_tagging.py` | Sequence Tagging using HMM & CRF |
| `ex12_machine_translation.py` | Machine Translation (Flask web app) |

## Requirements

```
pip install nltk scikit-learn tensorflow gensim flask sklearn-crfsuite keras-tuner
```

For Ex 12, run the script and open `http://127.0.0.1:5000` in your browser.
