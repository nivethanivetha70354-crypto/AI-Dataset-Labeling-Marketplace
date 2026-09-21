def calculate_quality(ai_label: str, final_label: str):
    if ai_label.strip().lower() == final_label.strip().lower():
        return 100.0

    return 0.0