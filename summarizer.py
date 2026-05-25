#!/usr/bin/env python3
"""MiMo Summarizer - Summarize any text or document."""
import os, argparse
from openai import OpenAI

client = OpenAI(api_key=os.getenv("MIMO_API_KEY"), base_url="https://api.xiaomimimo.com/v1")

def summarize(text, style="concise"):
    resp = client.chat.completions.create(model="mimo-v2.5-pro", messages=[
        {"role": "system", "content": f"Summarize in {style} style with bullet points."},
        {"role": "user", "content": text}])
    return resp.choices[0].message.content

if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("--text", required=True); p.add_argument("--style", default="concise")
    a = p.parse_args(); print(summarize(a.text, a.style))
