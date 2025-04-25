"""
TODO:
- Add a git post-commit hook to automatically update the vector store on each commit.
- The vector store shall contain, either the summary or the full diff+message into a vector and 
Metadata: commit hash, message, file path, timestamp, tags
- When the user queries the LLM, it searches the vector store and returns the most relevant commit.
- Potentially, the LLM should return:
    - The commit message and diff.
    - Linked issue/ticket (if available).
    - A summary of how the bug was fixed (auto-generated or extracted).
    - Option to view the full code change.

- The tool's value depends on the quality of its semantic search and the ease of 
integrating its suggestions into the developer's workflow
"""

