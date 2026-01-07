# Propositional Premise Verifier ⚖️

![Status](https://img.shields.io/badge/Status-Archived-red)
![Language](https://img.shields.io/badge/Language-Python-blue)
![Topic](https://img.shields.io/badge/Topic-Propositional_Logic-purple)

> **Note:** This project is archived. It serves as an implementation of a truth-functional propositional logic checker, determining the validity of arguments based on provided premises.

## 📖 Overview
This tool automates the verification of logical arguments. It takes a set of **Premises** and a **Conclusion**, constructs a truth table, and checks if the argument is **valid** (i.e., in every row where all premises are TRUE, the conclusion is also TRUE).

It parses standard logical operators to evaluate complex propositional forms:
* **Conjunction** ($\land$)
* **Disjunction** ($\lor$)
* **Implication** ($\to$)
* **Negation** ($\neg$)

## ⚙️ Logic Theory
The verifier is based on the definition of **Logical Entailment**:
$$\{P_1, P_2, ..., P_n\} \models C$$

An argument is **Valid** if and only if:
$$(P_1 \land P_2 \land ... \land P_n) \to C$$
is a **Tautology** (true in all possible truth-value assignments).

## 🚀 Usage

### Prerequisites
* Python 3.x

### Running the Verifier
```bash
# Clone the repository
git clone [https://github.com/srav-athina/Propositional-Premise-Verifier.git](https://github.com/srav-athina/Propositional-Premise-Verifier.git)

# Navigate to directory
cd Propositional-Premise-Verifier

# Run the verifier
python verifier.py
