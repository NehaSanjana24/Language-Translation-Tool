# Neural Mobile Web Hub: AI Translation Platform

A highly responsive, production-ready mobile-first web application that provides accurate, natural, and dialect-aware text translations across multiple languages—fully optimized for regional Indian languages like Telugu. 

This platform leverages high-capacity LLM infrastructures on the backend via the Groq LPU Cloud Architecture to ensure sub-second response times, coupled with specialized contextual instruction injections to maintain precise grammatical pronoun alignments.

### 🌐 Live Application Link
Experience the live application here: **[https://nehasanjana24.github.io/Language-Translation-Tool/](https://nehasanjana24.github.io/Language-Translation-Tool/)**

---

## 🚀 Key Features

* **Flagship AI Translation Engine:** Powered by the production-tier `llama-3.3-70b-versatile` model via Groq, ensuring optimal handling of complex sentences, idioms, and multi-clause phrasing.
* **Contextual Dialogue Mapping:** Features a hardcoded example framework injected straight into the user-prompt payload. This effectively prevents common translation bugs like pronoun-swapping or literal word-for-word string processing in short conversational snippets (e.g., "how are you" or "I hate you").
* **Instant, High-Clarity Audio (TTS):** Includes custom `window.speechSynthesis` caching routines that instantly clear previous playback pipelines, prevent clicking latency, and prioritize high-bitrate voice engines (such as Google Natural or premium local device packs).
* **Sleek Mobile-First Interface:** A responsive dashboard styled with Tailwind CSS, featuring automatic language swapping, text copying, and dynamic UI states during network requests.

---

## 🛠️ Architecture & Core Components

### 1. Frontend Web Client (`index.html`)
Handles user interactions, UI language states, browser clipboard integrations, and system-level audio streaming.

### 2. Live API Gateway (`Render Backend`)
Communicates seamlessly with a hosted endpoint to pass sanitized payloads directly to upstream LPU compute nodes securely:
`https://groq-translation-backend.onrender.com/translate`

---

## 💻 Tech Stack

* **Frontend UI:** HTML5, CSS3, Tailwind CSS (via official script browser runtime)
* **Iconography:** Lucide Icons Core Framework
* **AI Model Engine:** Meta Llama 3.3 70B Versatile
* **Hardware Accelerator:** Groq LPU (Language Processing Unit) Cloud API
* **Deployment Hosting:** GitHub Pages (Frontend Hub) & Render (Backend Architecture Gateway)

---

## 🔧 Getting Started & Local Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/nehasanjana24/Language-Translation-Tool.git](https://github.com/nehasanjana24/Language-Translation-Tool.git)
   cd Language-Translation-Tool
