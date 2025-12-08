import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def get_events():
    """Fetch all events from the database."""
    response = supabase.table('events').select("*").execute()
    return response.data

def create_event(name, description):
    """Create a new event."""
    response = supabase.table('events').insert({"name": name, "description": description}).execute()
    return response.data
