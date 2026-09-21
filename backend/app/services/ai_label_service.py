def generate_label_suggestion(text: str):
    text_lower = text.lower()

    positive_words = [
        "good",
        "great",
        "excellent",
        "love",
        "like",
        "amazing",
        "best",
        "happy",
        "awesome",
    ]

    negative_words = [
        "bad",
        "worst",
        "poor",
        "hate",
        "terrible",
        "awful",
        "disappointed",
        "waste",
    ]

    positive_score = sum(
        1 for word in positive_words
        if word in text_lower
    )

    negative_score = sum(
        1 for word in negative_words
        if word in text_lower
    )

    if positive_score > negative_score:
        label = "positive"
    elif negative_score > positive_score:
        label = "negative"
    else:
        label = "neutral"

    confidence = 0.90 if positive_score != negative_score else 0.60

    return {
        "suggested_label": label,
        "confidence": confidence,
    }