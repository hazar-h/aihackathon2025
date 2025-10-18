# 🖼️ Art.Decor.AI

### AI-Powered Home Décor Recommendation Platform

---

## 🌟 Problem Statement

Do you often struggle to **find wall art or décor that matches your room style, color palette, and lighting**?

You're not alone.

- **72%** of homeowners report difficulty finding décor that matches their existing interior.
- **58%** say they experience frustration from irrelevant décor recommendations when shopping online.
- **$18B** annual value loss due to returns and dissatisfaction with online home décor purchases.

**Art.Decor.AI** solves this problem by providing **AI-powered visual décor recommendations** that understand your **room style, lighting, and personal preferences**.

---

## 🧠 Introducing Art.Decor.AI

> “Your Personal AI Home Stylist”

Upload your **room photo**, describe your **theme**, or speak your query —  
Art.Decor.AI analyzes your space and suggests **perfect-matching wall art and décor** pieces curated to your aesthetic.

---

### 🎙️ 3 Types of User Inputs

| Input Type   | Description                                                                |
| ------------ | -------------------------------------------------------------------------- |
| 🖼️ **Photo** | Upload a room image for visual analysis (color palette, light, wall area). |
| ✍️ **Text**  | Describe your style (e.g., “Scandinavian living room with beige tones”).   |
| 🎤 **Voice** | Speak naturally (“Suggest a minimal art set for my bedroom wall”).         |

---

## 🤖 AI Agents Architecture

Art.Decor.AI is powered by **three collaborating AI Agents**, orchestrated by a **Decision Router**:

### 🧩 1. Vision-Match Agent

**Purpose:** Understands your room visually and matches compatible décor.

- Wall, window, and furniture detection (YOLOv8)
- Palette and lighting extraction (k-means + LAB)
- Aesthetic style matching (DINOv2 / CLIP embeddings)
- Personalized artwork recommendations from catalog

### 📈 2. Trend-Intel Agent

**Purpose:** Learns from current interior design trends.

- Retrieves trending art & décor styles from online sources
- Adapts model understanding to seasonal or local preferences
- Generates “style evolution” insights per user profile

### 📍 3. Geo-Finder Agent

**Purpose:** Finds décor items available near you.

- Uses Google Maps API to locate nearby art shops or galleries
- Integrates store availability and directions
- Suggests alternatives if online purchase unavailable

### 🧭 Decision Router

Formulates reasoning, routes tasks among agents, and summarizes final recommendations.

---

## 🧰 Key Features

| Feature                         | Description                                              |
| ------------------------------- | -------------------------------------------------------- |
| 💬 **Multimodal Chat**          | Interact using text, voice, or image.                    |
| 🧩 **AI Visual Analysis**       | Detects wall regions, light intensity, and room palette. |
| 🎨 **Personalized Suggestions** | Matches art & décor to your space and aesthetic.         |
| 🧠 **Stored User Profiles**     | Learns your style preferences over time.                 |
| 🏷️ **Smart Catalog Retrieval**  | Searches curated artworks and décor products.            |

---

## 🧱 System Architecture

**Frontend:**

- Next.js (TypeScript) + Tailwind CSS
- Upload, chat, and result visualization interfaces

**Backend:**

- FastAPI (Python) microservice
- Agents orchestrator & API router

**AI Model Stack:**  
| Model Type | Model Used |
|-------------|-------------|
| Object Detector | YOLOv8 |
| Image Embedder | DINOv2 / CLIP-ViT |
| Multimodal Reasoner | LLaVA / Llama 3 Vision |
| TTS (Voice Output) | Groq / OpenAI Whisper-TTS |

**Vector Database:** FAISS (Meta)  
**Metadata Database:** Supabase (PostgreSQL)  
**Cloud Hosting:** AWS / Render  
**Storage:** S3-compatible bucket (for room and art images)

---

## 🧩 Technical Architecture Diagram

![Alt text](images/art_decor_ai_architecture-v1.png "Optional Title")

## ![Alt text](images/art_decor_ai_architecture-v2.png "Optional Title")

## 🧩 Core Flow

1. **Upload Room Photo** → YOLOv8 detects walls & lighting.
2. **Extract Features** → Palette, brightness, style embeddings.
3. **Retrieve Artworks** → FAISS search for aesthetic match.
4. **Generate Reasoning** → LLM crafts design rationale (“why this fits”).
5. **Recommend Stores** → Trend & Geo agents fetch availability.
6. **Store Session** → Profile enrichment for future recommendations.

---

## 🧑‍💻 Tech Stack Summary

| Component          | Technology                            |
| ------------------ | ------------------------------------- |
| Frontend           | Next.js (TS), Tailwind CSS            |
| Backend            | FastAPI (Python)                      |
| Object Detection   | YOLOv8                                |
| Embedding Model    | DINOv2 / CLIP                         |
| Reasoning Model    | LLaVA / Llama 3 Vision                |
| Vector DB          | FAISS                                 |
| Database           | Supabase (PostgreSQL)                 |
| TTS / Voice        | Groq / Whisper                        |
| Cloud              | AWS S3 + Render / Vercel              |
| Agents Integration | Tavily API, Google Maps API, fetch.ai |

---

## 💡 Example User Interaction

**User:**

> "Show me wall art that matches my gray sofa and beige rug."

**Art.Decor.AI:**

1. Detects wall and sofa color palette.
2. Extracts mood tone (warm, minimal, neutral).
3. Suggests 3 art sets with matching tones.
4. Explains:
   > “These beige-toned abstracts complement your neutral palette and soften contrast against gray upholstery.”

---

## 💾 Data Schema

### Supabase Tables

| Table               | Fields                                                             |
| ------------------- | ------------------------------------------------------------------ |
| `artwork`           | id, title, brand, price, style_tags[], dominant_palette, image_url |
| `artwork_embedding` | id, vector[], artwork_id                                           |
| `room_upload`       | id, user_id, room_type, s3_url, palette_json, lighting_json        |
| `session`           | id, user_id, query_text, topk_ids[], chosen_id, rationale          |
| `user_profile`      | id, preferred_styles[], color_profile_json, budget_range           |

---

## 📅 Project Milestones

| Week | Milestone             | Deliverables                              |
| ---- | --------------------- | ----------------------------------------- |
| 1    | Setup & Dataset       | Supabase schema, 500+ artworks dataset    |
| 2    | Vision Agent          | Room detection & color palette extraction |
| 3    | Embedding & Retrieval | DINOv2 embeddings + FAISS search          |
| 4    | Advisor Agent         | Multimodal reasoning & LLM responses      |
| 5    | UI & Profile          | Chat UI, session persistence, trend agent |
| 6    | Final Presentation    | Live demo + architecture report           |

---

## 🧩 Evaluation Metrics

| Metric               | Description                                    |
| -------------------- | ---------------------------------------------- |
| 🎯 Relevance@K       | Visual match accuracy between room & décor     |
| 🎨 Palette Fit       | ΔE (color distance) between room & artwork     |
| 🗣️ Reasoning Quality | Clarity and contextual relevance of LLM output |
| ⚡ Latency           | Average response time < 3s                     |
| 💬 UX Rating         | Student / peer evaluation feedback             |

---

## 💰 Potential Monetization

- Affiliate commissions from décor brands
- Premium subscription for design consultation
- White-label API for home décor e-commerce sites

---

## 🧑‍🏫 Team Roles

| Role               | Responsibility                                 |
| ------------------ | ---------------------------------------------- |
| Vision Engineer    | Object detection, segmentation, color analysis |
| Backend Engineer   | FastAPI APIs, vector retrieval, orchestration  |
| AI Engineer        | Embedding & reasoning pipeline                 |
| Frontend Developer | Next.js chat, results, UX                      |
| PM / Designer      | Dataset curation, workflow, presentation       |

---

## 🚀 Demo Flow (Presentation Outline)

1. Upload a living room photo
2. System detects layout & wall palette
3. Retrieves matching art styles
4. Generates explanation + product links
5. Displays visualization + local store options

---

## 🔮 Future Enhancements

- Room layout mockups (AR visualization)
- Voice output (“Your AI stylist says…”)
- Multi-agent trend forecasting (color of the year)
- Integration with IKEA / Etsy / PosterStore APIs

---

---

### 🧩 Project Links

- **Frontend Repo:** `frontend/`
- **Backend Repo:** `backend/`
- **AI Models:** `ai-model/`
- **Docs:** `/docs/specs.md`

---

### 🧩 Sample UX

#### Landing Page

![Alt text](images/landing-page.png "Optional Title")

#### Start Page

![Alt text](images/home-page.png "Optional Title")

#### Upload and Analysis

![Alt text](images/page-2.png "Optional Title")

#### Recommendations

![Alt text](images/page-3.png "Optional Title")

#### Details and Reasoning

![Alt text](images/page-4.png "Optional Title")

#### Local Stores

![Alt text](images/page-5.png "Optional Title")

#### Chat

![Alt text](images/page-6.png "Optional Title")
