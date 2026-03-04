import sys
def analyze(text):
    text = text.lower()
    pos = sum(1 for w in ['love', 'great', 'best', 'awesome', 'amazing'] if w in text)
    neg = sum(1 for w in ['bad', 'worst', 'hate', 'terrible', 'slow', 'fail'] if w in text)
    if pos > neg: print("[BASELINE] Positive Sentiment Detected")
    elif neg > pos: print("[BASELINE] Negative Sentiment Detected - Escalation Required")
    else: print("[BASELINE] Neutral Sentiment")
if __name__ == "__main__":
    if len(sys.argv) > 1: analyze(sys.argv[1])
