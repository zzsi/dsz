# Market Entry Compliance Navigator

This repository contains an early prototype for a Streamlit application that assists companies planning to expand into new markets. Users provide details about their target market, industry, business model, and data handling practices. The app then calls OpenAI's API to generate:

- Key compliance areas to consider
- A high-level compliance roadmap that can be downloaded as a Markdown report

## Running the App
1. Install dependencies:
   ```bash
   pip install -r requirements.txt streamlit
   ```
2. Set the required environment variables:
   - `OPENAI_API_KEY` – API key for OpenAI
   - `PASSCODE` – passcode required to access the app
3. Start the Streamlit server:
   ```bash
   streamlit run prototype/app.py
   ```

## Deployment
The prototype can be hosted on [Streamlit Community Cloud](https://streamlit.io/cloud). After logging in with the Streamlit CLI, deploy the app with:

```bash
streamlit login
streamlit deploy prototype/app.py
```

In the future we may integrate GitHub Actions to automate this deployment workflow.

## Code Structure
- `prototype/app.py` – multi-step Streamlit interface that collects user context and generates compliance guidance using the OpenAI API.
- `prototype/llm.py` – helper functions for calling language models.
- `overseas_expansion_resources.md` – reference material for market expansion.

## Limitations
- Only OpenAI integration is implemented; `chat_gemini` is a stub.
- Minimal validation and error handling in the Streamlit flows.
- Dependency list is incomplete (Streamlit is not in `requirements.txt`).
- No automated tests.
- Deployment is manual through the Streamlit CLI; no automated pipeline yet.

