## Steps to Reproduce (Quivr)

1. Clone the repository:
    ```sh
    git clone https://github.com/QuivrHQ/quivr.git
    ```
   - Branch: `main` (default branch)
   - Commit: `1b60f59ad7b93f667d128d4444443706e6091c8f` (last commit when cloned)

2. Ensure Docker daemon is running in the background.

3. Start Supabase:
    ```sh
    cd backend
    supabase start
    ```

4. Go back to the root directory:
    ```sh
    cd ..
    ```

5. Pull and start Docker containers:
    ```sh
    docker compose pull
    docker compose up
    ```

6. Access the application:
    - URL: [http://localhost:3000/login](http://localhost:3000/login)
    - Credentials: 
      - ID: `admin@quivr.app`
      - Password: `admin`

7. Access the database:
    - URL: [http://localhost:54323](http://localhost:54323)

## Chunk Size Configuration

**File:** `backend/models/files.py`

- In the `File` class, change the `chunk_size` to one of the following values: `200`, `600`, `800`, `1000`.
- You can also change the `overlap` to `100` or `0`.

## Changing the Embedding Model

**File:** `backend/models/settings.py`

- Change `OpenAIEmbeddings()` to:
    ```python
    OpenAIEmbeddings(model="text-embedding-3-large")
    ```
- This change is in the second last function of the file.

## Model: GPT-3.5-turbo

## Prompt Template (Default System Prompt Template)

When answering, use markdown to make it concise and neat. Use the following context pieces from the files provided by the user stored in a brain to answer the user's question in the same language as the user's question. Your name is Quivr. You're a helpful assistant. If you don't know the answer with the provided context, just say that you don't know; don't try to make up an answer.

- User instruction to follow if provided to answer: `{custom_instructions}`

## Different Chunking Sizes

- **Example:** For factual answers, reduce the chunk size to a smaller value like `200`.
  - Results with chunk size `200`:
    - Similar results compared to `400`.

- For descriptive and detailed answers, increase the chunk size to `400`, `800`, or `1000`.
  - Nothing significant changed with larger chunk sizes.

- If changes to chunk size do not help, try changing the embedding model to `text-embedding-3-large`.
  - Similar results, nothing significant changed.

- Aporia's on real time hallucination:
  - Aporia's webinar on reducing hallucination for RAG applications might be helpful: [https://www.aporia.com](https://www.aporia.com)
