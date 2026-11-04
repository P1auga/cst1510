# CST1510 — Python Coursework

Seven weeks of Python coursework: walkthrough notebooks, a lab per week, extra practice
projects, and the solutions to the weekly programming problem sheets.

## Layout

Every week follows the same shape:

```text
Week 04/
├── walkthroughs/              the taught material, one folder per topic
│   ├── 01_Lists/              W04T01_walkthrough.ipynb + examples/
│   ├── 02_Dictionaries/
│   ├── 03_Files/
│   ├── 04_Handling_Errors/
│   └── 05_Putting_It_Together/
├── lab/                       W04_Lab.ipynb, template.py, warmup/, notes/
├── problems/                  solutions from the week's problem sheet
└── extra_projects/            optional practice projects
```

| Week | Subject | Topics | Lab | Problems | Extras |
|------|---------|--------|-----|----------|--------|
| 01 | Values, Types and Input-Output | 4 | `W01_Lab.ipynb` | 12 | 2 |
| 02 | Decisions and Loops | 4 | `W02_Lab.ipynb` | 18 | 4 |
| 03 | Functions and Modules | 4 | `W03_Lab.ipynb` | 11 | 3 |
| 04 | Lists, Dictionaries and Files | 5 | `W04_Lab.ipynb` | 37 | 4 |
| 05 | Classes and Objects | 3 | `W05_Lab.ipynb` | 9 | 1 |
| 06 | Pandas | 4 | `W06_Lab.ipynb` | 18 | 3 |
| 07 | Strings and Text Manipulation | 4 | `W07_Lab.ipynb` | 14 | 2 |

119 problem solutions, 19 extra projects, 35 notebooks, 225 Python files.

## Running it

```bash
source .venv/bin/activate        # pandas and matplotlib are installed here
cd "Week 06/problems"
python W06T01_load_explore.py
```

Scripts read their data from the `data/` folder beside them, so run them from their own
directory. Notebooks run from their own folder for the same reason.

## Notes

- `Week NN/lab/notes/` holds the photographed cheat-sheet pages. The lab notebooks link
  to them rather than embedding the images, so the files stay small.
- Three notebooks fail on purpose, because their exercise is to read the error:
  `Week 03/lab/W03_Lab.ipynb` drill 9, `Week 04/walkthroughs/01_Lists/W04T01_walkthrough.ipynb`
  cell 23, and `Week 05/walkthroughs/01_Classes_and_Objects/W05T01_walkthrough.ipynb` cell 15.
- `.venv/` is excluded from git; recreate it with `python3 -m venv .venv` and
  `pip install pandas matplotlib`.
