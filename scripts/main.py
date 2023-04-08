"""
# Photopea integration for a1111-sd-webui
Under development

dev notes:
- [Photopea API docs](https://www.photopea.com/api/)
"""

import gradio as gr
import sys
import io
from pathlib import Path
from fastapi import FastAPI
from modules import scripts, script_callbacks, shared

# const variables
APP_URL = "https://www.photopea.com/"


def init(demo: gr.Blocks, app: FastAPI) -> None:
    pass


def on_ui_tabs():
    iframe: str = """
    <iframe src="{app_url:s}" id="oe-photopea" allow="clipboard-read; clipboard-write" style="width: 100%; height: 80vh; min-height: 800px; resize: vertical;"></iframe>"""
    with gr.Blocks(analytics_enabled=False) as photopea:
        photopea_app = gr.HTML(iframe.format(app_url=APP_URL))
        photopea = photopea_app
    return (photopea, "Photopea", "photopea"),


script_callbacks.on_app_started(init)
script_callbacks.on_ui_tabs(on_ui_tabs)
