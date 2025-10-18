# Art.Decor.AI - User Workflows & System Outputs

## Workflow 1: Photo-Based Room Analysis

### User Journey

```
1. User Opens App
   ↓
2. Selects "Upload Photo" Option
   ↓
3. Captures/Selects Room Image
   ↓
4. System Processes Image
   ↓
5. Receives AI Recommendations
   ↓
6. Browses Artworks
   ↓
7. Views Details & Local Stores
   ↓
8. Makes Purchase Decision
```

### AI Processing Pipeline

```
INPUT: Room Photo
  ↓
[Vision-Match Agent]
  ├─ YOLOv8 Object Detection
  │  ├─ Detects walls, furniture, windows
  │  └─ Identifies wall dimensions & angles
  ├─ Color Palette Extraction (k-means)
  │  ├─ Dominant colors: Gray, Beige, White
  │  └─ Color palette: Neutral with warm tones
  ├─ Lighting Analysis
  │  ├─ Natural light intensity: High
  │  └─ Light source direction: North-facing window
  └─ Style Recognition (DINOv2/CLIP)
     └─ Detected style: Minimalist Modern
  ↓
[Retrieval System]
  ├─ FAISS Vector Search
  │  └─ Match similar artwork embeddings
  └─ Filter by: Color palette, Style, Budget
  ↓
[LLM Reasoning Engine]
  └─ Generate design rationale: "Why this works for your space"
  ↓
OUTPUT: Top 5 Artwork Recommendations + Explanations
```

### AI Output Example

```json
{
  "room_analysis": {
    "wall_color": "Warm Gray (#A89968)",
    "lighting": "Natural, North-facing",
    "room_type": "Living Room",
    "detected_style": "Minimalist Modern",
    "dimensions": "15ft W x 12ft H wall"
  },
  "recommendations": [
    {
      "id": 1,
      "title": "Abstract Serenity",
      "reason": "Complements your warm gray walls with soft beige abstracts. Natural light will bring out the subtle texture.",
      "color_match_score": 0.94,
      "style_match_score": 0.89,
      "price": 129.99,
      "nearby_stores": 2
    }
  ]
}
```

---

## Workflow 2: Text-Based Style Description

### User Journey

```
1. User Opens App
   ↓
2. Selects "Describe Your Style"
   ↓
3. Types: "Scandinavian living room, lots of plants,
          natural wood furniture, prefer abstract art"
   ↓
4. System Extracts Keywords & Preferences
   ↓
5. AI Generates Personalized Recommendations
   ↓
6. User Refines Filters (Budget, Color)
   ↓
7. Explores Recommendations
   ↓
8. Adds to Wishlist
```

### AI Processing Pipeline

```
INPUT: User Text Query
  ↓
[NLP Processing - LLM]
  ├─ Extract Keywords: Scandinavian, Plants, Wood, Abstract
  ├─ Infer Style: Nordic Minimalism
  ├─ Color Inference: Whites, Naturals, Muted Greens
  └─ Budget Extraction: Mid-range
  ↓
[Trend-Intel Agent]
  ├─ Check trending Scandinavian designs
  ├─ Seasonal color palettes
  └─ Popular abstract styles in Nordic category
  ↓
[Vector Search]
  ├─ Search embeddings for "Scandinavian abstract art"
  ├─ Filter by color: Naturals & Whites
  └─ Rank by popularity & relevance
  ↓
[LLM Reasoning]
  ├─ Generate personalized explanations
  └─ Connect recommendations to user preferences
  ↓
OUTPUT: 12 Curated Recommendations with Style Explanations
```

### AI Output Example

```json
{
  "user_preferences": {
    "style": "Scandinavian",
    "keywords": ["minimalist", "plants", "wood", "abstract"],
    "inferred_colors": ["natural_white", "muted_green", "soft_gray"],
    "budget_range": 80-200
  },
  "recommendations": [
    {
      "id": 1,
      "title": "Nordic Minimalist Abstract",
      "why_selected": "This piece perfectly embodies Scandinavian minimalism. The abstract elements add visual interest while maintaining the clean aesthetic you love. Pairs beautifully with natural wood furniture.",
      "style_tags": ["Scandinavian", "Minimalist", "Abstract"],
      "color_harmony": ["white", "natural_gray", "soft_green"],
      "design_notes": "Works exceptionally well in rooms with plants - the abstract forms complement organic shapes"
    }
  ]
}
```

---

## Workflow 3: Voice-Based Natural Conversation

### User Journey

```
1. User Taps Microphone Icon
   ↓
2. Says: "I have a bedroom with soft pink walls
          and I want something calming and modern"
   ↓
3. System Transcribes & Analyzes Voice
   ↓
4. AI Understands Intent & Context
   ↓
5. Generates Recommendations
   ↓
6. Speaks Recommendations Back (TTS)
   ↓
7. User Asks Follow-up Questions
   ↓
8. Conversational Refinement
```

### AI Processing Pipeline

```
INPUT: Voice Audio
  ↓
[Whisper API - Speech-to-Text]
  └─ Transcribe: "I have a bedroom with soft pink walls..."
  ↓
[NLP Understanding - LLM]
  ├─ Entity Recognition:
  │  ├─ Room Type: Bedroom
  │  ├─ Color: Soft Pink
  │  └─ Mood: Calming
  ├─ Intent: Seeking calm, modern artwork
  ├─ Tone: Conversational & Personal
  └─ Context: Personal bedroom space
  ↓
[Vision-Match Agent]
  ├─ Match soft pink color palette
  ├─ Infer calming color combinations
  └─ Recommend modern, soothing styles
  ↓
[LLM Response Generation]
  ├─ Create conversational response
  ├─ Explain recommendations naturally
  └─ Suggest follow-up questions
  ↓
[TTS - Text-to-Speech]
  └─ Generate natural voice response
  ↓
OUTPUT: Voice Response + Visual Recommendations
  └─ Groq TTS: "I found beautiful modern pieces that complement
               soft pink walls. They feature calming blues and
               whites that create a serene atmosphere..."
```

### AI Output Example

```json
{
  "transcribed_input": "I have a bedroom with soft pink walls and I want something calming and modern",
  "understood_context": {
    "room": "Bedroom",
    "wall_color": "Soft Pink",
    "desired_mood": "Calming",
    "style_preference": "Modern",
    "confidence": 0.96
  },
  "voice_response": {
    "text": "Great! I found perfect modern pieces for your soft pink bedroom. I'm showing you artworks in cool blues and whites that create a calming atmosphere. These will complement your walls beautifully.",
    "audio_file": "response_001.mp3",
    "follow_up_suggestions": [
      "Would you like to see more minimalist styles?",
      "What's your budget range?",
      "Do you prefer abstract or landscape art?"
    ]
  },
  "recommendations": [...]
}
```

---

## Workflow 4: Refinement Through Chat Interaction

### User Journey

```
1. User Views Initial Recommendations
   ↓
2. Opens Chat with AI Stylist
   ↓
3. User: "Can you show me something more colorful?"
   ↓
4. AI Understands Refinement Request
   ↓
5. Filters & Re-ranks Recommendations
   ↓
6. Shows More Vibrant Options
   ↓
7. User: "I like this one but want to know about nearby stores"
   ↓
8. AI Activates Geo-Finder Agent
   ↓
9. Shows Local Availability
```

### AI Processing Pipeline - Refinement Loop

```
USER MESSAGE: "Can you show something more colorful?"
  ↓
[LLM Understanding]
  ├─ Recognize refinement request
  ├─ Extract constraint: "More colorful"
  └─ Adjust search parameters
  ↓
[Dynamic Re-ranking]
  ├─ Query FAISS for vibrant color embeddings
  ├─ Filter current recommendations
  └─ Surface high-saturation artworks
  ↓
[Trend-Intel Agent]
  └─ Check trending colorful designs
  ↓
[LLM Response Generation]
  ├─ Explain why these are more colorful
  ├─ Show color comparison
  └─ Maintain consistency with original preferences
  ↓
OUTPUT: Updated Recommendations + Explanation

─────────────────────────────────────────

SUBSEQUENT USER MESSAGE: "How far is store XYZ?"
  ↓
[Geo-Finder Agent]
  ├─ Get user location (with permission)
  ├─ Query Google Maps API
  ├─ Calculate distance & directions
  ├─ Get store hours & availability
  └─ Retrieve store contact info
  ↓
[LLM Response]
  └─ Natural language response with store details
  ↓
OUTPUT: Store Location Info + Directions
```

### AI Output Example

```json
{
  "user_message": "Can you show me something more colorful?",
  "refinement_analysis": {
    "request_type": "Filter Adjustment",
    "new_constraint": "High Saturation Colors",
    "previous_constraint": "Neutral Palette",
    "adjustment_confidence": 0.94
  },
  "updated_recommendations": [
    {
      "id": 7,
      "title": "Vibrant Rainbow Abstract",
      "color_saturation": "High",
      "why_better": "This piece brings vibrant energy while still maintaining modern elegance. The bold colors will create a striking focal point in your space.",
      "color_palette": ["#FF6B6B", "#4ECDC4", "#FFE66D"],
      "comparison_note": "Compared to previous suggestions, this has 3x higher color saturation"
    }
  ],
  "follow_up": "These are definitely more colorful! Would you like to see even bolder options, or should we stick with this vibrancy level?"
}
```

---

## Workflow 5: Complete Purchase Journey

### User Journey

```
1. User Selects Favorite Artwork
   ↓
2. Views Detailed Product Info
   ↓
3. AI Explains Design Rationale
   ↓
4. Checks Local Store Availability
   ↓
5. Compares Prices
   ↓
6. User: "Take me to the nearest store"
   ↓
7. Geo-Finder Provides Directions
   ↓
8. User Visits Store
   ↓
9. Makes Purchase
   ↓
10. Adds Review & Photo to Profile
```

### AI Processing Pipeline - Purchase Workflow

```
USER ACTION: Click "View in Stores"
  ↓
[Geo-Finder Agent]
  ├─ Get user location
  ├─ Query Google Maps for relevant stores
  ├─ Check store inventory (API integration)
  ├─ Get store hours & contact
  └─ Calculate distances & ETAs
  ↓
[Vision-Match Agent]
  ├─ Confirm product details
  ├─ Generate comparison with similar products
  └─ Provide alt options if unavailable
  ↓
[LLM Response Generation]
  ├─ Create detailed product narrative
  ├─ Generate personalized recommendations
  └─ Summarize store locations
  ↓
OUTPUT: Store List + Directions + Stock Status

─────────────────────────────────────────

USER ACTION: Post-Purchase (Uploads new room photo)
  ↓
[Vision-Match Agent]
  ├─ Analyze before/after
  ├─ Detect purchased artwork in new photo
  └─ Extract new design preferences
  ↓
[User Profile Update]
  ├─ Add to purchase history
  ├─ Update style preferences
  └─ Improve future recommendations
  ↓
[Feedback Loop]
  └─ Enhance ML models with new data
```

### AI Output Example

```json
{
  "product_selection": {
    "id": 1,
    "title": "Abstract Harmony",
    "price": 129.99
  },
  "store_availability": [
    {
      "store_name": "Modern Art Gallery",
      "distance": "0.8 mi",
      "status": "In Stock",
      "address": "123 Art Street, City",
      "hours": "10 AM - 8 PM",
      "directions_url": "https://maps.google.com/...",
      "phone": "(555) 123-4567"
    },
    {
      "store_name": "Design Hub",
      "distance": "2.3 mi",
      "status": "Limited Stock (1 piece)",
      "address": "456 Design Ave, City",
      "hours": "11 AM - 6 PM",
      "directions_url": "https://maps.google.com/...",
      "phone": "(555) 234-5678"
    }
  ],
  "purchase_confirmation": {
    "method": "In-store or Online",
    "estimated_delivery": "3-5 business days",
    "return_policy": "30-day returns"
  }
}
```

---

## Workflow 6: Trend-Based Recommendations

### User Journey

```
1. User Browses "Trending Now" Section
   ↓
2. AI Shows Seasonal Color Trends
   ↓
3. User Explores Trending Styles
   ↓
4. Discovers New Design Movements
   ↓
5. Asks: "What's popular in my area?"
   ↓
6. AI Shows Local Design Trends
   ↓
7. User Finds Trending Pieces
```

### AI Processing Pipeline - Trend Analysis

```
DAILY/WEEKLY EXECUTION: Trend Analysis
  ↓
[Trend-Intel Agent]
  ├─ Web Scraping:
  │  ├─ Pinterest trending searches
  │  ├─ Interior design blogs
  │  ├─ Design magazines
  │  └─ Social media hashtags
  ├─ Analysis:
  │  ├─ Color trend extraction
  │  ├─ Style movement identification
  │  ├─ Seasonal pattern recognition
  │  └─ Regional preferences
  └─ Integration:
     ├─ Update vector database
     ├─ Re-rank artworks
     └─ Create seasonal collections
  ↓
[Geo-Intel - Regional Customization]
  ├─ Identify user location
  ├─ Extract regional design trends
  ├─ Surface location-specific artworks
  └─ Show local artist preferences
  ↓
[LLM Report Generation]
  ├─ Create trend narratives
  ├─ Explain why trends matter
  └─ Connect to user preferences
  ↓
OUTPUT: Trending Artworks + Explanations + Local Insights
```

### AI Output Example

```json
{
  "trending_analysis": {
    "season": "Fall 2024",
    "top_colors": [
      {"color": "Warm Terracotta", "trend_score": 0.92},
      {"color": "Sage Green", "trend_score": 0.89},
      {"color": "Deep Navy", "trend_score": 0.85}
    ],
    "top_styles": [
      {"style": "Maximalist Abstract", "trend_score": 0.88},
      {"style": "Nature-Inspired", "trend_score": 0.86}
    ]
  },
  "local_insights": {
    "region": "San Francisco Bay Area",
    "dominant_style": "Modern Minimalist with Tech Influence",
    "popular_colors": ["Cool Grays", "Charcoal Black", "Accent Copper"],
    "local_artists": 24,
    "trending_locally": "Sustainable Art & Recycled Materials"
  },
  "personalized_trends": [
    {
      "trend": "Warm Terracotta with Geometric Patterns",
      "why_for_you": "Matches your minimalist style while embracing this season's warmth trend",
      "recommended_artworks": [...]
    }
  ]
}
```

---

## Data Flow Summary

```
┌─────────────────┐
│  User Inputs    │
├─────────────────┤
│ • Photo Upload  │
│ • Text Query    │
│ • Voice Input   │
│ • Chat Messages │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────┐
│  AI Processing Agents       │
├─────────────────────────────┤
│ 1. Vision-Match Agent       │
│ 2. Trend-Intel Agent        │
│ 3. Geo-Finder Agent         │
│ + LLM Reasoning             │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│  Data Storage & Retrieval   │
├─────────────────────────────┤
│ • Vector DB (FAISS)         │
│ • PostgreSQL (Metadata)     │
│ • AWS S3 (Images)           │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│  AI Outputs                 │
├─────────────────────────────┤
│ • Recommendations (JSON)    │
│ • Explanations (Text)       │
│ • Store Info (Map Data)     │
│ • Voice Response (Audio)    │
└─────────────────────────────┘
```

---
