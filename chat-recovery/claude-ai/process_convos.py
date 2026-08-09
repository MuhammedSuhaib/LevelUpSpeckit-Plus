import json
import os
import re
import glob

def sanitize_filename(name):
    clean = re.sub(r'[\\/*?:"<>|]', "", name).strip()
    return clean if clean else "Untitled"

def extract_clean_text(msg):
    text = msg.get("text", "")
    if not text:
        content_list = msg.get("content", [])
        text_parts = []
        for item in content_list:
            if isinstance(item, dict) and item.get("type") == "text":
                text_parts.append(item.get("text", ""))
        text = "\n".join(text_parts)
    return text.strip()

def process_conversations(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    with open(input_file, "r", encoding="utf-8") as f:
        conversations = json.load(f)

    valid_count = 0
    skipped_empty = 0

    for idx, conv in enumerate(conversations, start=1):
        uuid = conv.get("uuid", f"chat_{idx}")
        name = conv.get("name") or "Untitled"
        created_at = conv.get("created_at")
        updated_at = conv.get("updated_at")
        
        messages = conv.get("chat_messages", [])
        turns = []
        turn_number = 1
        i = 0

        while i < len(messages):
            msg = messages[i]
            sender = msg.get("sender")

            if sender == "human":
                user_req = extract_clean_text(msg)
                assistant_resp = ""
                
                file_attachments = []
                for f in msg.get("files", []):
                    fname = f.get("file_name")
                    if fname:
                        file_attachments.append(fname)

                if i + 1 < len(messages) and messages[i + 1].get("sender") == "assistant":
                    assistant_resp = extract_clean_text(messages[i + 1])
                    i += 1
                
                # Only keep turns that have actual text content or file attachments
                if user_req or assistant_resp or file_attachments:
                    turn_data = {
                        "turn": turn_number,
                        "request": user_req,
                        "response": assistant_resp
                    }
                    if file_attachments:
                        turn_data["files"] = file_attachments
                    
                    turns.append(turn_data)
                    turn_number += 1
            i += 1

        # ONLY save file if there is at least 1 real non-empty turn
        if turns:
            valid_count += 1
            clean_name = sanitize_filename(name)[:40]
            filename = f"{valid_count:03d}_{clean_name}_{uuid[:8]}.json"
            filepath = os.path.join(output_dir, filename)

            conv_data = {
                "id": uuid,
                "title": name,
                "created_at": created_at,
                "updated_at": updated_at,
                "total_turns": len(turns),
                "turns": turns
            }

            with open(filepath, "w", encoding="utf-8") as out:
                json.dump(conv_data, out, indent=2, ensure_ascii=False)
        else:
            skipped_empty += 1

    print(f"Done! Filtered out {skipped_empty} empty conversations. Exported {valid_count} real non-empty chats to '{output_dir}/'.")

if __name__ == "__main__":
    # Clean output folder first
    existing = glob.glob("convos/*.json")
    for e in existing:
        os.remove(e)

    process_conversations("conversations.json", "convos")
