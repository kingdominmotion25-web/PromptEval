"""
PromptEval - Prompt Quality Scoring Engine
Version 0.1
"""

from dataclasses import dataclass


@dataclass
class PromptScore:
    clarity: int
    context: int
    constraints: int
    output_format: int

    @property
    def total(self):
        return (
            self.clarity
            + self.context
            + self.constraints
            + self.output_format
        )


def evaluate_prompt(prompt: str) -> PromptScore:
    """
    Simple rule-based evaluator.
    Scores each category from 0–25.
    """

    clarity = 25 if len(prompt) > 40 else 10

    context = (
        25
        if any(word in prompt.lower() for word in ["context", "background", "audience"])
        else 10
    )

    constraints = (
        25
        if any(word in prompt.lower() for word in ["must", "only", "under", "limit"])
        else 10
    )

    output_format = (
        25
        if any(word in prompt.lower() for word in ["json", "table", "list", "markdown"])
        else 10
    )

    return PromptScore(
        clarity=clarity,
        context=context,
        constraints=constraints,
        output_format=output_format,
    )
