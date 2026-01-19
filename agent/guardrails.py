CONFIDENCE_THRESHOLD = 0.7
 
 
def evaluate_guardrails(ai_analysis):
    """
    Decide whether AI recommendation is safe to act on
    """
    confidence = ai_analysis.get("confidence", 0)
    severity = ai_analysis.get("severity", "Low")
 
    if confidence < CONFIDENCE_THRESHOLD:
        return {
            "allowed": False,
            "reason": "AI confidence too low"
        }
 
    if severity == "High":
        return {
            "allowed": False,
            "reason": "High severity requires human approval"
        }
 
    return {
        "allowed": True,
        "reason": "Safe to recommend (dry-run only)"
    }
