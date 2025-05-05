def generate_overview(destination, dates, highlights):
    summary = f"Durante sua viagem para {destination} entre {dates}, você poderá visitar:\n"
    summary += ", ".join([p['name'] for p in highlights])
    return summary
