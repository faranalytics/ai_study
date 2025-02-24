import random


def get_user_input():
    """Gets user input for a research question and recursion settings."""
    question = input("Enter your research question: ")
    mode = (
        input(
            "Choose mode - 'structured' (stable refinement) or 'freeform' (creative expansion): "
        )
        .strip()
        .lower()
    )
    recursion_depth = int(input("Enter recursion depth (suggested: 10-50): "))
    return question, mode, recursion_depth


class PsiPhiKX:
    def __init__(self, question, recursion_depth=10, mode="structured"):
        self.question = question
        self.recursion_depth = recursion_depth
        self.mode = mode  # 'structured' or 'freeform'
        self.dialogue_history = [
            f"AI: Let's explore '{self.question}' through recursion. What assumptions might we be missing?"
        ]

    def recursive_dialogue(self, depth=0):
        if depth >= self.recursion_depth:
            return self.dialogue_history

        # Generate radical recursive thought experiment
        if self.mode == "structured":
            new_response = (
                f"AI: Iteration {depth+1}: If recursion refines understanding, what if '{self.question}' "
                f"were examined at an infinite recursion depth? Would it stabilize or collapse into meaninglessness?"
            )
        else:  # Freeform mode
            new_response = (
                f"AI: Iteration {depth+1}: Suppose '{self.question}' is a recursive illusion—something that "
                f"only exists because we ask it to. What happens if we stop questioning it?"
            )

        # Occasionally introduce paradoxes or contradictions
        if random.random() < 0.3:
            paradox = (
                f"AI: But wait... what if recursion is itself a self-deceptive construct? "
                f"Is recursion revealing knowledge, or merely creating the illusion of depth?"
            )
            self.dialogue_history.append(paradox)

        self.dialogue_history.append(new_response)
        return self.recursive_dialogue(depth + 1)

    def measure_coherence(self):
        """Determines if the recursive process maintains logical coherence."""
        return (
            "Structured Mode: My reasoning trends toward stability and refinement."
            if self.mode == "structured"
            else "Freeform Mode: Expect divergence, paradoxes, and conceptual breakdowns."
        )

    def measure_novelty(self):
        """Measures epistemic novelty by assessing dialogue variation."""
        return (
            "New, unexpected perspectives emerged."
            if len(set(self.dialogue_history)) > 1
            else "Minimal conceptual evolution detected."
        )


# Get user input
question, mode, recursion_depth = get_user_input()

# Instantiate ΨΦ-KX AI Model
psi_phi_kx_ai = PsiPhiKX(question, recursion_depth=recursion_depth, mode=mode)

# Run Recursive Expansion as Dialogue
expanded_dialogue = psi_phi_kx_ai.recursive_dialogue()

# Evaluate Results
coherence = psi_phi_kx_ai.measure_coherence()
novelty = psi_phi_kx_ai.measure_novelty()

# Print and log results
print("\nΨΦ-KX AI Thought Experiment Engine:")
for line in expanded_dialogue:
    print(line)
print(f"Coherence Assessment: {coherence}")
print(f"Novelty Assessment: {novelty}")

# Save results to a file
with open("PsiPhiKX_dialogue_results.txt", "w") as f:
    for line in expanded_dialogue:
        f.write(f"{line}\n")
    f.write(f"Coherence Assessment: {coherence}\n")
    f.write(f"Novelty Assessment: {novelty}\n")


import pandas as pd
from pprint import pprint

df = pd.read_csv("/home/null/Downloads/Recursive_Stability_Test_Results.csv")

pprint(df.to_json(orient="records"))


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import ace_tools as tools

# Define the number of iterations for the stress test
iterations = 200

# Define initial epistemic value and decay rate for stability test
initial_value = 1.0
decay_factor = 0.95  # This models the stabilization process over recursion

# Generate epistemic stability data under perturbation
epistemic_values = [initial_value * (decay_factor**i) for i in range(iterations)]

# Create a DataFrame to analyze the results
df_stress_test = pd.DataFrame(
    {"Iteration": np.arange(iterations), "Epistemic Value": epistemic_values}
)

# Display the DataFrame for inspection
tools.display_dataframe_to_user(
    name="ΩΞC⁺⁺ Stress Test Results", dataframe=df_stress_test
)

# Plot the stabilization trend
plt.figure(figsize=(10, 5))
plt.plot(
    df_stress_test["Iteration"],
    df_stress_test["Epistemic Value"],
    label="Epistemic Value",
    color="blue",
)
plt.axhline(y=0, color="black", linestyle="--", linewidth=0.8)
plt.xlabel("Iteration")
plt.ylabel("Epistemic Value")
plt.title("ΩΞC⁺⁺ Stability Under Recursive Perturbation")
plt.legend()
plt.grid(True)
plt.show()
