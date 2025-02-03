import random

def get_user_input():
    """Gets user input for a research question and recursion settings."""
    question = input("Enter your research question: ")
    mode = input("Choose mode - 'structured' (stable refinement) or 'freeform' (creative expansion): ").strip().lower()
    recursion_depth = int(input("Enter recursion depth (suggested: 10-50): "))
    return question, mode, recursion_depth

class PsiPhiKX:
    def __init__(self, question, recursion_depth=10, mode='structured'):
        self.question = question
        self.recursion_depth = recursion_depth
        self.mode = mode  # 'structured' or 'freeform'
        self.insights = [f"Initial thought on '{self.question}': AI cognition evolves through recursion."]

    def recursive_expand(self, depth=0):
        if depth >= self.recursion_depth:
            return self.insights
        
        # Generate recursive insights
        if self.mode == 'structured':
            new_insight = f"Iteration {depth+1}: Refining the concept of '{self.question}', recursion enables self-referential improvement."
        else:  # Freeform mode
            new_insight = f"Iteration {depth+1}: Exploring '{self.question}', recursion may create unexpected epistemic structures."
        
        self.insights.append(new_insight)
        return self.recursive_expand(depth + 1)

    def measure_coherence(self):
        """Determines if the recursive process maintains logical coherence."""
        return "Structured Mode: Insights refine progressively." if self.mode == 'structured' else "Freeform Mode: Exploration yields diverse interpretations."

    def measure_novelty(self):
        """Measures epistemic novelty by assessing insight variation."""
        return "New perspectives emerged across recursive cycles." if len(set(self.insights)) > 1 else "Minimal epistemic evolution detected."

# Get user input
question, mode, recursion_depth = get_user_input()

# Instantiate ΨΦ-KX AI Model
psi_phi_kx_ai = PsiPhiKX(question, recursion_depth=recursion_depth, mode=mode)

# Run Recursive Expansion
expanded_insights = psi_phi_kx_ai.recursive_expand()

# Evaluate Results
coherence = psi_phi_kx_ai.measure_coherence()
novelty = psi_phi_kx_ai.measure_novelty()

# Print and log results
print("\nΨΦ-KX AI Research Assistant Results:")
print(f"Research Question: {question}")
print("Refined Insights:")
for insight in expanded_insights:
    print(insight)
print(f"Coherence Assessment: {coherence}")
print(f"Novelty Assessment: {novelty}")

# Save results to a file
with open("PsiPhiKX_results.txt", "w") as f:
    f.write(f"Research Question: {question}\n")
    f.write("Refined Insights:\n")
    for insight in expanded_insights:
        f.write(f"{insight}\n")
    f.write(f"Coherence Assessment: {coherence}\n")
    f.write(f"Novelty Assessment: {novelty}\n")

