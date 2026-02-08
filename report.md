## Challenges

One of the primary challenges of using an LLM is **prompt design**. Obtaining accurate and consistent outputs requires carefully constraining the model’s behavior through explicit instructions and examples. Small ambiguities in the prompt can lead to incorrect field extraction, missing values, or outputs that violate the expected JSON schema. As a result, prompt engineering became an iterative process, requiring repeated refinement to reduce errors and improve consistency.

Another challenge is handling **ambiguity within the source documents themselves**. AD texts often contain conditional language, exceptions, or references to external documents. While the LLM can interpret such context reasonably well, the extracted results may still reflect uncertainty or partial interpretation, especially when the source text is not explicit.

---

## Limitations

I do not consider the LLM output to be fully reliable on its own. Instead, I would further formalize the system is designed with a **human-in-the-loop mindset**, similar in spirit to active learning workflows. The LLM generates structured candidate outputs, but these are expected to be reviewed and validated by a human, particularly in ambiguous or safety-critical scenarios. This design choice acknowledges the limitations of fully automated decision-making in regulatory and aviation contexts.

Cost is another important limitation. Unlike simple logic-based solutions, the LLM-based approach is **not cheap**, as it relies on an external API (Google Gemini). This makes the approach less suitable for large-scale or continuous processing unless combined with cost-mitigation strategies such as selective invocation, batching, or caching.

---

## Trade-offs and Design Decisions

The main trade-off in this project lies between **simplicity and adaptability**. A rule-based approach is cheaper, faster, and easier to reason about, but it lacks robustness when faced with diverse document structures. The LLM-based approach introduces higher cost and complexity, but it offers significantly better adaptability and reduces dependence on document-specific templates.

I chose an LLM-based solution because the core requirement of this task was **automation across heterogeneous documents**, not optimization for a single known format. While Vision-Language Models (VLMs) could be considered for handling scanned or visually complex PDFs, the documents used in this project are text-extractable, making text-based LLM processing a more practical and efficient choice.

Overall, the system prioritizes **adaptability and interpretability over full automation**. By combining LLM-based extraction with structured outputs and human oversight, the approach balances practical automation with the caution required for regulatory document analysis.
