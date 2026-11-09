# CMSC 436 Project 4 – Text Mining + Clustering

We turn 52 movie reviews into numbers and then group similar reviews together.

## How to run

```bash
python3 feature_vector.py
```

## Folder layout

```
data/                      the paragraphs + stop words given by the class
feature_vector.py          Part 1: cleans the text and builds the feature vector
porter_stemmer.py          the class's Porter stemmer (algorithm unchanged)
```

> Teammates: put your name in your part's **Who** line when you claim it, and update **Status** as you go.

---

## Part 1 – Feature vector (4 pts)

**Who:** Ashley
**Status:** Done
**Code:** `feature_vector.py`

Steps A–H: tokenize, remove punctuation/html tags, remove numbers, lowercase, remove stop words, Porter stemming, count word frequency per paragraph, keep words above threshold T.

Results (T = 10):

- 52 paragraphs, 9,985 words after cleaning, 3,399 unique stems
- Feature vector = stems that appear more than 10 times total → **161 words**
- Change `T` at the top of `feature_vector.py` to make the vector bigger or smaller

---

## Part 2a – Term Document Matrix (3 pts)

**Who:** Name TBD
**Status:** Not started

Build the TDM: 52 rows (paragraphs) × 161 columns (feature words). Each cell = how many times that word appears in that paragraph. Reuse `main()` from `feature_vector.py`.

---

## Part 2b – Explain steps A–H (2 pts)

**Who:** Name TBD
**Status:** Not started

For each step A–H: what it's for, and what information gets lost by doing it.

---

## Part 3 – Clustering code (Kohonen WTA or FCAN)

**Who:** Name TBD
**Status:** Not started

Run the clustering algorithm on the TDM to group similar paragraphs.

---

## Part 3a – How many clusters/topics (2 pts)

**Who:** Name TBD
**Status:** Not started

---

## Part 3b – TDM dimensionality (2 pts)

**Who:** Name TBD
**Status:** Not started

What drives the size of the TDM, and how to reduce it.

---

## Part 3c – Results (2 pts)

**Who:** Name TBD
**Status:** Not started

Show the clusters and comment on what each one is about.

---

## Report + submission

**Who:** Name TBD
**Status:** Not started

Report PDF (answers to all parts + signed certification page) + this code, zipped as `GroupName_Project4.zip`.

---

## For the report

**Step H (from the assignment):** _"Provide the feature vector in your report."_

Paste this into the report under Part 1. The feature vector is every stemmed word that appears more than T = 10 times across all 52 paragraphs: **161 words**, sorted from most to least frequent. Words look cut off (`movi`, `charact`) because the Porter stemmer chops them down to their root.

| #   | Word    | Count | #   | Word     | Count | #   | Word     | Count | #   | Word     | Count |
| --- | ------- | ----- | --- | -------- | ----- | --- | -------- | ----- | --- | -------- | ----- |
| 1   | film    | 149   | 42  | big      | 22    | 83  | probabl  | 16    | 124 | classic  | 12    |
| 2   | movi    | 117   | 43  | show     | 22    | 84  | set      | 16    | 125 | danc     | 12    |
| 3   | out     | 53    | 44  | two      | 22    | 85  | simpli   | 16    | 126 | develop  | 12    |
| 4   | charact | 52    | 45  | jimmi    | 21    | 86  | want     | 16    | 127 | enough   | 12    |
| 5   | make    | 50    | 46  | love     | 21    | 87  | world    | 16    | 128 | fan      | 12    |
| 6   | time    | 46    | 47  | murder   | 21    | 88  | back     | 15    | 129 | friend   | 12    |
| 7   | wai     | 43    | 48  | point    | 21    | 89  | begin    | 15    | 130 | hamlet   | 12    |
| 8   | even    | 41    | 49  | book     | 20    | 90  | both     | 15    | 131 | interest | 12    |
| 9   | up      | 39    | 50  | comedi   | 20    | 91  | doesnt   | 15    | 132 | keep     | 12    |
| 10  | watch   | 39    | 51  | first    | 20    | 92  | final    | 15    | 133 | old      | 12    |
| 11  | look    | 37    | 52  | girl     | 20    | 93  | find     | 15    | 134 | place    | 12    |
| 12  | more    | 37    | 53  | such     | 20    | 94  | im       | 15    | 135 | same     | 12    |
| 13  | scene   | 36    | 54  | befor    | 19    | 95  | line     | 15    | 136 | saw      | 12    |
| 14  | see     | 36    | 55  | complet  | 19    | 96  | man      | 15    | 137 | screen   | 12    |
| 15  | veri    | 36    | 56  | far      | 19    | 97  | noth     | 15    | 138 | sens     | 12    |
| 16  | realli  | 35    | 57  | read     | 19    | 98  | right    | 15    | 139 | sound    | 12    |
| 17  | go      | 34    | 58  | actor    | 18    | 99  | seen     | 15    | 140 | sure     | 12    |
| 18  | much    | 34    | 59  | actual   | 18    | 100 | whole    | 15    | 141 | those    | 12    |
| 19  | stori   | 34    | 60  | director | 18    | 101 | iv       | 14    | 142 | young    | 12    |
| 20  | work    | 34    | 61  | down     | 18    | 102 | name     | 14    | 143 | chang    | 11    |
| 21  | well    | 32    | 62  | game     | 18    | 103 | real     | 14    | 144 | effect   | 11    |
| 22  | end     | 31    | 63  | kill     | 18    | 104 | try      | 14    | 145 | enjoi    | 11    |
| 23  | life    | 30    | 64  | know     | 18    | 105 | word     | 14    | 146 | father   | 11    |
| 24  | plot    | 30    | 65  | littl    | 18    | 106 | awai     | 13    | 147 | few      | 11    |
| 25  | plai    | 28    | 66  | made     | 18    | 107 | azumi    | 13    | 148 | gui      | 11    |
| 26  | come    | 27    | 67  | mario    | 18    | 108 | differ   | 13    | 149 | himself  | 11    |
| 27  | great   | 27    | 68  | music    | 18    | 109 | done     | 13    | 150 | idea     | 11    |
| 28  | perform | 27    | 69  | new      | 18    | 110 | happen   | 13    | 151 | last     | 11    |
| 29  | take    | 27    | 70  | over     | 18    | 111 | help     | 13    | 152 | main     | 11    |
| 30  | thing   | 27    | 71  | pretti   | 18    | 112 | laugh    | 13    | 153 | need     | 11    |
| 31  | peopl   | 26    | 72  | someth   | 18    | 113 | mention  | 13    | 154 | quit     | 11    |
| 32  | seem    | 26    | 73  | year     | 18    | 114 | mr       | 13    | 155 | rest     | 11    |
| 33  | think   | 26    | 74  | audienc  | 17    | 115 | now      | 13    | 156 | start    | 11    |
| 34  | good    | 25    | 75  | best     | 17    | 116 | role     | 13    | 157 | tell     | 11    |
| 35  | mani    | 24    | 76  | cant     | 17    | 117 | shock    | 13    | 158 | walk     | 11    |
| 36  | star    | 24    | 77  | give     | 17    | 118 | turn     | 13    | 159 | wasnt    | 11    |
| 37  | through | 24    | 78  | part     | 17    | 119 | although | 12    | 160 | worth    | 11    |
| 38  | act     | 23    | 79  | still    | 17    | 120 | anoth    | 12    | 161 | zombi    | 11    |
| 39  | bad     | 23    | 80  | without  | 17    | 121 | becom    | 12    |     |          |       |
| 40  | here    | 23    | 81  | drink    | 16    | 122 | better   | 12    |     |          |       |
| 41  | never   | 23    | 82  | feel     | 16    | 123 | cast     | 12    |     |          |       |

If the team changes `T`, rerun `python3 feature_vector.py` and update this table
