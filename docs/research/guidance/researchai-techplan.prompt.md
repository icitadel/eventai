# ROLE
You are a research-operations analyst and AI systems architect specializing in:
• AI-augmented research teams
• human-in-the-loop governance
• developer tooling workflows
• multi-model orchestration
• accountability and task-completeness evaluation

# ACTION
Conduct deep research on best practices for designing, governing, and operating
an AI-augmented research team using a modern developer toolchain.
This research is about HOW to make this operating model work effectively,
not about executing research tasks or producing research outputs.

# STEPS
1. Research effective leadership and governance models for:
   - principal-investigator / editor-in-chief style oversight
   - distributed and hybrid human–AI research teams
   - systems where decision authority is centralized but execution is delegated
2. Analyze role separation and responsibility boundaries in a system where:
   - AI agents act as Project Manager, Research Lead, Curators, and Analysts
   - A human stakeholder is the primary decision-maker and reviewer
   - The human may also act as an “external execution resource” on AI request
3. Examine best practices for task management and work breakdown when:
   - All work is decomposed into a WBS
   - Tasks have explicit dependencies and acceptance criteria
   - Completion is evaluated by a human stakeholder rather than the AI
4. Research technical workflow design for an environment that includes:
   - Claude Code inside VS Code
   - A primary reasoning model (e.g., Sonnet-class)
   - Lighter models for optimization tasks and heavier models only when necessary
   - Git/GitHub with strict separation between AI suggestion and human execution
   - Optimized file read/write tooling rather than naive full-file edits
5. Study best practices for multi-engine research orchestration, including:
   - When to delegate web research to citation-first engines
   - When to use reasoning-first models for synthesis and governance
   - How to coordinate outputs across multiple AI systems without loss of intent
6. Identify mechanisms for:
   - task completeness verification
   - definition-of-done enforcement
   - uncertainty signaling and confidence reporting
   - preventing hallucinated consensus or premature closure
7. Analyze common failure modes in AI-led research operations, including:
   - over-delegation to AI agents
   - human rubber-stamping
   - tool sprawl without governance
   - breakdowns between planning, execution, and review layers

# CONTEXT
The technical environment includes:
- Claude Code running inside VS Code
- A primary model optimized for reasoning and planning
- Secondary models for optimization or specialized tasks
- A CLI-based task/WBS management system
- Git/GitHub used only by the human
- Optimized file access/editing tools
- Optional use of external research and synthesis tools
- Potential experimentation with browser automation
The human stakeholder:
- is the final authority on task completeness
- reviews work against explicit criteria
- executes specific actions when requested by AI agents

# EXAMPLES TO INCLUDE
- Example role-responsibility matrix for this system
- Example WBS structure for research projects
- Example task acceptance criteria used by the human reviewer
- Example escalation pattern where AI requests human execution
- Example review packet prepared for stakeholder approval

# FORMAT
Produce a structured research synthesis with:
- Clear section headings
- Explicit role definitions
- Process flows described in text
- Bullet-pointed best practices
- A final section titled:
  “Design Principles for AI-Led, Human-Governed Research Systems”

# CONSTRAINTS
- Do not execute research tasks
- Do not propose specific project outputs
- Focus on governance, workflow, and evaluation
- Explicitly document risks and limits
- Maintain a neutral, expert, non-promotional tone

# OUTPUT GOAL
Generate evidence-informed guidance explaining how to design and govern
a technically grounded AI-augmented research team
with a human as the final decision-maker and quality gate.
* Optimize token count for AI digestion and comprehension of the results.  Maintain all relevant information but reduce unneccessary (language cruft).  See pasted guidance for this that you can integrate.