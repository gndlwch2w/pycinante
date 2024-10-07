from typing import Dict, Any, Optional

__all__ = ["is_valexp", "eval_valexp"]

def is_valexp(exp: str) -> bool:
    """
    Return the expression is a valid value expression, i.e. {variable}.
    """
    return exp.startswith("{") and exp.endswith("}")

def eval_valexp(exp: str, context: Optional[Dict[str, Any]] = None) -> Any:
    """
    Return the value that is evaluated from the value expression.
    """
    return eval(exp[1:-1], context) if is_valexp(exp) else exp
