# Daily Python Workflow

Use this file for every new day. It is the practical checklist for continuing the repository from Day 17 onward.

## 1. Create the day

Create this structure:

```text
days/day-17/
  README.md
  project/
    README.md
    main.py
    tests/
notes/day-17.md
```

Use the next day number and a meaningful project name when the idea is clear. Do not add course metadata or copied solution files.

For Days 1-16, the repository keeps earlier file names such as `task.py` where they contain your original practice code. Do not rename working files only to match this newer template.

## 2. Study one Python topic

Before coding, write the topic in `days/day-XX/README.md`:

- What Python feature was studied.
- Why it is useful.
- One small example written from memory.
- One question or uncertainty to investigate.

Keep the explanation in your own words. The course is the source for instruction; this repository is the record of your understanding and practice.

## 3. Define a small project

In the project README, write:

- The problem the project solves.
- The first version's three to five features.
- What inputs it accepts.
- What output or result it produces.
- What is deliberately out of scope for today.

Choose a project small enough to finish a working version in one focused session.

## 4. Build the first version

Write the project in `main.py` and split logic into functions or classes when that makes the code clearer. Prefer readable code over clever code. Handle invalid input without an unexplained crash.

## 5. Test and improve

Run the program with normal input, empty input, invalid input, and an edge case. Add focused tests in `tests/` when the project contains reusable logic.

Then make one improvement beyond the first working version, such as better validation, clearer structure, or a useful feature.

## 6. Update the daily note

Add `notes/day-XX.md` with:

- Python topics learned.
- Technical terms explained in plain language.
- A small code example.
- What went wrong and how it was fixed.
- What the project taught you.
- One next step for review.

## 7. Finish the day

Before committing, check:

- The project runs from its documented command.
- The README matches the current code.
- The main behavior was tested manually.
- Tests pass, if tests exist.
- No passwords, tokens, virtual environments, or `__pycache__` files are included.
- `git status` shows only intentional changes.

Use a focused commit message:

```text
Day 17: build project name
Day 17: add input validation
Day 17: document lessons learned
```

## Where information belongs

| Location | Purpose |
| --- | --- |
| `README.md` | Repository overview and long-term progress |
| `days/README.md` | Rules for organizing daily folders |
| `days/day-XX/README.md` | That day's topic, goal, and project summary |
| `days/day-XX/project/README.md` | How to use that specific project |
| `notes/day-XX.md` | Learning explanation, terminology, examples, and reflection |
| `DAILY_CHECKLIST.md` | The repeatable process for every future day |