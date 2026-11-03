# Chapter 8 Review: Creating and Connecting Objects

Fork of [polla-fattah/ood-agile-book](https://github.com/polla-fattah/ood-agile-book). Edited file: [`content/book/chapter-08.md`](content/book/chapter-08.md). Every change in the chapter has a **Reviewer note** next to it explaining why.

## What the chapter covers

Chapter 8 (Week 7) teaches five Gang-of-Four patterns. It does not present them as a catalogue. The chapter's question is *"which responsibility needs a boundary, and what is the smallest design that makes it clear?"*

| Pattern | Example in the chapter | Used in the running project? |
|---|---|---|
| Factory Method | `ExportJob` with a `createExporter()` hook, compared with a simple factory | No, isolated example |
| Abstract Factory | `ReceiptFamily` giving matching heading and body renderers | No, isolated example |
| Builder | Immutable `ReportRequest` built step by step and validated | No, isolated example |
| **Adapter** | `LegacyDirectoryAdapter` translates the university directory's codes (`S`/`T`, `Y`/`N`, null, failures) into the app's `Borrower` | **Yes**, the one pattern the project adopts |
| Decorator | `AuditedSender` and `RetryOnceSender`, where wrapping order changes the result | No, isolated example |

Its strongest point is that it teaches **when not to use a pattern** (Section 8.7) and treats failure semantics (absence vs. outage) as part of the design.

## Changes made and why

| # | Where | Change | Why |
|---|---|---|---|
| 1 | Intro | One 90-word sentence of learning outcomes became a bullet list | Easier to scan, and the five pattern names are visible |
| 2 | Intro | A ~200-word "what to read / what to do" paragraph became a table, and "63-invocation baseline" is now explained | The paragraph mixed section numbers, step numbers and two projects. The jargon was never defined |
| 3 | 8.2 Factory Method | Added `PlainJob`/`HtmlJob` code beside `simpleExporter` | The text says the two differ in *where the next change lands* but showed only one of them |
| 4 | 8.3 Abstract Factory | Added code and a class diagram (new Figure 8.2) | It was the only creational pattern with no code and no diagram, and its main idea (one factory, matching roles) is structural |
| 5 | 8.5 Adapter | Added the core `find()` method | This is a core section with no code. The method can now be checked row by row against the translation table |
| 6 | 8.5 Adapter | One sentence on object vs. class Adapter | GoF describes both, and the chapter used "object Adapter" without saying what the alternative is |
| 7 | 8.5 Adapter | The book-wide chapter roadmap became a short aside | It interrupted the Adapter explanation |
| 8 | 8.6 Decorator | Added `RetryOnceSender` code and the two nesting orders in code | "Audit outside retry" was hard to picture. Two constructor lines make it concrete |
| 9 | 8.11 Questions | Pointer to model answers in the companion | Nothing told students the answers exist |
| 10 | Appendix A, slides | Figure 8.2 renumbered to 8.3 | Keeps cross-references correct after inserting the new figure |

All added code is copied from the book's own companion file (`content/companion/chapter-08.md`), so it matches the tested project.

## Feedback not applied (left for the author)

- **Prose density.** Many paragraphs stack hedges ("does not… does not… is not"). They are accurate but tiring. Fewer, stronger sentences would read better.
- **Admin text in the chapter body.** Lines about LOs, the module descriptor and the midterm scope belong in an instructor box, not the opening.
- **Slides.** The new Abstract Factory figure is not in the slide deck yet.
