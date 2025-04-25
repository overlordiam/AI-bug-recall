# 🛠️ MCP Bug Resolver Tool - PRD

## 1. Overview

This product is a **personal bug resolution assistant**, powered by a **local MCP server** that integrates directly with MCP-compatible IDEs (e.g., Cursor, Windsurf).  
It allows developers to ask questions like “How did I fix this error before?” and retrieves previous bug fixes using Git commit history, code context, and embeddings.

---

## 2. Goals

- Allow developers to retrieve past bug fixes from commit history and code context.  
- Seamlessly integrate with IDEs that support MCP.  
- Automatically activate upon IDE startup without user configuration.  
- Present helpful summaries and code snippets inside the IDE.

---

## 3. Non-Goals

- Web-based access outside the IDE.  
- Handling bugs across multiple machines (initial release is local-only).  
- Real-time LLM code suggestions (handled by IDE).

---

## 4. Features

### 4.1 IDE Integration (MCP)
- Register the tool with the IDE's MCP client.  
- Listen for specific trigger phrases (e.g., "how did I fix", "bug", "error").  
- Activate when the IDE opens a project or file.  
- Send structured responses (summary + file/line + snippet).

### 4.2 Bug Resolver Agent (MCP Node Graph)
- Accepts natural language questions.  
- Searches a vector DB containing:
  - Commit messages  
  - Code diffs  
  - Bug fix notes  
- Retrieves file path, diff, timestamp, and nearby code.  
- Uses an LLM to generate a natural answer.
- Hybrid search, combine vector search (semantic similarity) with keyword filters (e.g., error codes, stack traces).

### 4.3 Local Knowledge Graph
- Built by indexing commit history and codebase.  
- Updated on each commit (optional Git hook or watcher).  
- Stores metadata for bug-related commits (e.g., “fix”, “bug”, “error”).

### 4.4 Option to search through multiple repos (Optional)
- Currently, it searches for the resolved bug under the current git repo only.
- The above can be extended to multiple repos by prompting the user for a connection with github.

---

## 5. MCP Graph Spec (Simplified)

```yaml
graph:
  id: bug_resolution_graph

nodes:
  - input_router
  - bug_history_agent
  - summarizer_agent
  - fallback_agent
  - output
```

Each node is a tool or LLM-based agent handling:
- Input classification  
- Retrieval from vector DB  
- Summarization  
- Output formatting

---

## 6. User Flow

### IDE Side:
1. User opens IDE (Cursor/Windsurf).  
2. IDE sends MCP init and registers available agents.  
3. User types: “How did I fix the JWT expiry bug?”  
4. IDE sends request via MCP to local tool.

### Tool Side:
1. Routes to bug history agent.  
2. Searches for related commits and retrieves diffs.  
3. Sends context to LLM summarizer.  
4. Sends result back to IDE.

---

## 7. Technical Stack

| Component         | Tech Used                        |
|------------------|----------------------------------|
| IDE Integration   | MCP Protocol (native)            |
| Server Runtime    | MCP Graph Runtime (e.g., LangGraph) |
| Data Indexing     | GitPython, AST parsing           |
| Vector Store      | Chroma / Weaviate (local)        |
| LLM               | Local model (Mistral/Phi-2) or API |
| Language          | Python (or Node for tools)       |
