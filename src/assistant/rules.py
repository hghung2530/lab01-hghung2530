import csv
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "offices.csv"

def load_offices():
    offices = {}
    if DATA_PATH.exists():
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 3:
                    name, room, hours = [col.strip() for col in row[:3]]
                    offices[name.lower()] = {
                        "name": name,
                        "room": room,
                        "hours": hours,
                    }
    return offices

OFFICES = load_offices()

def reply(query: str) -> str:
    query_str = query.strip()
    query_lower = query_str.lower()
    
    if not query_str:
        return "Please ask a question."
    
    if any(greet in query_lower for greet in ["hi", "hello", "hey"]):
        return "Hello! Ask me where an office is, or when it opens."
    
    # Check offices first
    offices = load_offices()
    for key, info in offices.items():
        if key in query_lower:
            return f"{info['name']}: room {info['room']}, open {info['hours']}."

    if "help" in query_lower:
        return "I can help you locate offices and check their opening hours. Try asking: 'where is IT helpdesk?'"
            
    return "I'm sorry, I don't understand your request."
