def build_review_prompt(
    diff_text: str,
    retrieved_context: list[object],
    rules_context: list[str] | None = None,
) -> str:
    raise NotImplementedError


def build_fix_prompt(
    finding: object,
    surrounding_code: str,
) -> str:
    raise NotImplementedError
