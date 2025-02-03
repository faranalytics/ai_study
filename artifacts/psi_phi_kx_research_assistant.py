import numpy as np
import random

def get_user_input():
    """Gets user input for a research question and recursion settings."""
    question = input("Enter your research question: ")
    mode = input("Choose mode - 'structured' (stable refinement) or 'freeform' (creative expansion): ").strip().lower()
    recursion_depth = int(input("Enter recursion depth (suggested: 10-50): "))
    return question, mode, recursion_depth

class PsiPhiKX:
    def __init__(self, question, recursion_depth=50, perturbation_factor=0.2, stabilization_threshold=0.05, mode='structured'):
        self.question = question
        self.recursion_depth = recursion_depth
        self.perturbation_factor = perturbation_factor
        self.stabilization_threshold = stabilization_threshold
        self.mode = mode  # 'structured' or 'freeform'
        self.knowledge_state = [random.uniform(0.3, 0.7) for _ in range(5)]  # Initial metastable knowledge seeds

    def recursive_expand(self, depth=0):
        if depth >= self.recursion_depth:
            return self.knowledge_state
        
        # Introduce recursive transformation with stabilization
        if self.mode == 'structured':
            new_state = [x + np.sin(depth * x) * self.perturbation_factor for x in self.knowledge_state]
        else:  # Freeform mode
            new_state = [x + random.uniform(-self.perturbation_factor, self.perturbation_factor) for x in self.knowledge_state]
        
        # Apply self-stabilization boundary
        self.knowledge_state = [max(self.stabilization_threshold, min(1 - self.stabilization_threshold, x)) for x in new_state]
        
        return self.recursive_expand(depth + 1)

    def measure_coherence(self):
        """Determines if the recursive process maintains logical coherence."""
        return np.var(self.knowledge_state) < 0.1  # Low variance suggests stabilization

    def measure_novelty(self, previous_state):
        """Measures epistemic novelty by comparing changes in recursive iterations."""
        return np.linalg.norm(np.array(self.knowledge_state) - np.array(previous_state)) > 0.05

# Get user input
question, mode, recursion_depth = get_user_input()

# Instantiate ΨΦ-KX AI Model
psi_phi_kx_ai = PsiPhiKX(question, recursion_depth=recursion_depth, perturbation_factor=0.2, stabilization_threshold=0.05, mode=mode)

# Run Recursive Expansion
previous_state = psi_phi_kx_ai.knowledge_state.copy()
expanded_state = psi_phi_kx_ai.recursive_expand()

# Evaluate Results
coherence = psi_phi_kx_ai.measure_coherence()
novelty = psi_phi_kx_ai.measure_novelty(previous_state)

# Print and log results
print("\nΨΦ-KX AI Research Assistant Results:")
print(f"Research Question: {question}")
print(f"Final Knowledge State: {expanded_state}")
print(f"Coherence Maintained: {coherence}")
print(f"Novelty Emerged: {novelty}")

# Save results to a file
with open("PsiPhiKX_results.txt", "w") as f:
    f.write(f"Research Question: {question}\n")
    f.write(f"Final Knowledge State: {expanded_state}\n")
    f.write(f"Coherence Maintained: {coherence}\n")
    f.write(f"Novelty Emerged: {novelty}\n")

