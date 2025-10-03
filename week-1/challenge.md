# One-Hour Guided Lab: Tutor Finder (Streamlit + pandas + numpy)

## Overview  

### Scenario: “Tutor Finder – Match Students with the Right Tutors”

You’re building a tiny Streamlit app (pandas + numpy) to help parents/students find after-school tutors. The app loads a small CSV of tutors, lets users filter, ranks tutors by skills match + years of experience + rating, and shows results.

What learners practice
- Data cleaning and feature extraction (skills parsing, numeric coercion) with Pandas
- Simple scoring with NumPy (e.g., Jaccard on skills + Gaussian around target experience + normalized rating)
- Streamlit UI with filters/table
- Dockerize the app
- Optional LLM integration for message drafting

---

## Task 1: Load & Inspect (≈10 min)  
**Goal:** load the CSV into pandas and check for issues.  

- Read the CSV (`pd.read_csv`).  
- Inspect with `.info()`, `.head()`.  
- Look for:  
  - `years_experience`: values like `"3+"` or `"five"`.  
  - `hourly_rate`: with `$` or `PKR`.  
  - `rating`: blanks, out-of-range values.  
  - `subjects`: inconsistent casing/spaces.  

**Hints:**  
- Use `pd.to_numeric(..., errors="coerce")`.  
- Strip symbols with regex (`.str.replace`).  
- Normalize strings with `.str.strip().str.lower()`.  

**Reflection:**  
- What % of rows failed parsing?  
- Should you drop bad rows or coerce them?  

---

## Task 2: Feature Extraction (≈10 min)  
**Goal:** create clean, analysis-ready columns.  

- `skills_set`: split subjects on commas → set.  
- `years_num`: integer, default 0.  
- `rate_num`: numeric hourly rate.  
- `rating_norm`: scale to `[0,1]`.  

**Reflection:**  
- Which features matter most for ranking?  
- Should raw + cleaned columns both be kept?  

---
## Task 3: Scoring Tutors (≈15 min)  
**Goal:** assign a score based on skills, experience, and rating.  

- **Skills match (Jaccard):**  
jaccard = |A ∩ B| / |A ∪ B|

markdown
Copy code
- **Experience proximity (Gaussian):**  
exp_score = exp( - (y - t)^2 / (2σ^2) )

markdown
Copy code
Use σ=2.  
- **Rating:** normalized to [0,1].  
- **Final score:**  
score = 0.5 * skills + 0.3 * exp + 0.2 * rating

markdown
Copy code

**Reflection:**  
- Does adding experience/rating improve ranking vs skills-only?  
- Should weights be fixed or user-tunable?  


---

## Task 4: Streamlit UI (≈15 min) (Optional) 
**Goal:** interactive filtering & ranking.  

**Sidebar filters:**  
- City (multiselect).  
- Subject (multiselect).  
- Min years (slider).  
- Max rate (slider).  
- Target years (slider for Gaussian).  

**Main area:**  
- Count of matching tutors.  
- Table (Name, Subjects, Years, Rate, Rating, Score).  
- Expander for tutor bio/details.  

**Reflection:**  
- Is latency acceptable (<200ms)?  
- What happens when no tutors match?  

---

## Task 5: Bonus — Outreach Message (≈5 min) (Optional) 
**Goal:** generate a polite draft to a tutor.  

- Inputs: tutor name, subjects, city, years.  
- Prompt:  
*“Draft a <120-word outreach message to {tutor}, polite, concise, ask about availability.”*  
- Run via **Mistral-7B** (Ollama or Hugging Face).  

**Reflection:**  
- Compare to a hand-written template — is LLM better?  
- How to handle weird/messy tutor bios?  

---

## Task 6: Stretch — Dockerize (≈5–10 min)  (Optional) 
**Goal:** run anywhere.  

- Base: `python:3.10-slim`.  
- Install: `pandas`, `numpy`, `streamlit`.  
- Copy app + CSV.  
- Run:  
streamlit run app.py --server.port=8501 --server.address=0.0.0.0

markdown
Copy code

**Reflection:**  
- Does everyone on the team get reproducible runs?  
- Is image size reasonable?  

---

## Wrap-up Reflection (5 min)  
- Where did most errors come from: cleaning or scoring?  
- What was your simplest working baseline?  
- If you had 2 more hours, would you improve **data**, **scoring**, or **UI**?  

---

## 📚 Documentation Reference  

### pandas
- [to_numeric](https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html)  
- [string methods](https://pandas.pydata.org/docs/user_guide/text.html)  

### NumPy
- [exp](https://numpy.org/doc/stable/reference/generated/numpy.exp.html)  
- [array operations](https://numpy.org/doc/stable/user/quickstart.html)  

### Streamlit
- [st.selectbox / multiselect](https://docs.streamlit.io/library/api-reference/widgets/st.multiselect)  
- [st.slider](https://docs.streamlit.io/library/api-reference/widgets/st.slider)  
- [st.dataframe](https://docs.streamlit.io/library/api-reference/data/st.dataframe)  

### Jaccard similarity
- [Definition & examples](https://en.wikipedia.org/wiki/Jaccard_index)
- [Code Snippers](https://www.geeksforgeeks.org/data-science/how-to-calculate-jaccard-similarity-in-python/)

###  Docker
- [Dockerizing Streamlit](https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker)  
### Mistral-7B
- [Hugging Face model card](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)  
- [Ollama quickstart](https://ollama.ai/library/mistral)  

---
