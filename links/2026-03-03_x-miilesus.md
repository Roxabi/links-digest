---
title: "Amazing prompt from @astronomerozge1"
source: "https://x.com/miilesus/status/2028911446474600850?s=20"
date: 2026-03-03
tags: ["image generation prompt", "black and white photography", "facial expression grid", "photobooth style"]
platform: x
author: "@miilesus"
summary: "The prompt requests a 4x4 black-and-white photobooth grid featuring an adult woman with consistent identity across various facial expressions."
---
Amazing prompt from @astronomerozge1 

Prompt: {
  "generation_request": {
    "meta_data": {
      "task_type": "black_and_white_photobooth_expression_grid_4x4",
      "language": "en",
      "priority": "highest",
      "version": "v1.0_BW_PHOTOBOOTH_EXPRESSIONS_4X4"
    },
    "input": {
      "mode": "image_to_image",
      "reference_image_usage": "very_high",
      "preserve_identity": true,
      "preserve_facial_features": true,
      "preserve_hairstyle": true,
      "notes": "Use the reference as the primary anchor. Create a dark black-and-white photobooth-style expression grid. Keep the same adult woman identity and hair. Each panel should show a different facial expression. Minimal background, direct photobooth flash look, natural skin texture."
    },
    "output": {
      "aspect_ratio": "1:1",
      "resolution": "ultra_high",
      "num_images": 1,
      "layout": {
        "type": "grid",
        "rows": 4,
        "cols": 4,
        "gutter": "thin",
        "panel_consistency": "high"
      },
      "sharpness": "crisp_photobooth",
      "grain": "subtle_analog_bw"
    },
    "scene": {
      "concept": "classic photobooth contact sheet with expressive faces",
      "environment": "plain neutral backdrop, no props",
      "lighting": {
        "style": "direct photobooth flash",
        "key_light": "front flash, slightly hard but flattering",
        "shadows": "soft short shadows behind subject",
        "avoid": "cinematic side light, dramatic backgrounds"
      },
      "camera": {
        "lens": "50mm",
        "distance": "tight head-and-shoulders framing",
        "focus": "eyes sharp in every panel"
      }
    },
    "subject": {
      "type": "adult woman",
      "wardrobe": "simple strapless or bare-shoulder photobooth look (no logos)",
      "hair": "keep same hairstyle across all panels",
      "makeup": "minimal, natural",
      "anatomy_rules": "correct facial proportions, no warped eyes/mouth"
    },
    "expression_set": {
      "panel_01": "natural smile, soft eye contact",
"panel_02": "head tilted back laughing, joyful open smile",
"panel_03": "serious / slightly annoyed stare, lips pressed",
"panel_04": "playful wink with subtle smirk",

"panel_05": "tongue out, playful teasing expression",
"panel_06": "wide surprised eyes, mouth open in shock",
"panel_07": "kissy lips / duck face",
"panel_08": "hot expression",

"panel_09": "hands framing face, playful wide eyes",
"panel_10": "blowing a kiss toward camera",
"panel_11": "serious neutral expression, direct stare",
"panel_12": "soft confident smile",

"panel_13": "gentle closed-lip smile",
"panel_14": "chin resting on hand, pouty playful look",
"panel_15": "slightly confused or skeptical expression",
"panel_16": "eyes closed, peaceful happy smile",

"panel_17": "disgusted / scrunched face",
"panel_18": "tight eyes closed grin, expressive smile",
"panel_19": "side smile with eyes closed, content expression",
"panel_20": "neutral serious face, calm direct gaze"
    },
    "style": {
      "color": "pure black and white",
      "contrast": "medium-high",
      "background": "flat gray",
      "finish": "slight photobooth grain, clean edges"
    },
    "quality_control": {
      "identity_lock": "strict",
      "hands_priority": "high",
      "avoid": [
        "extra fingers",
        "missing fingers",
        "deformed hands",
        "warped face",
        "uneven eyes",
        "melted mouth",
        "plastic skin",
        "text",
        "watermark",
        "logo"
      ]
    },
    "negative_prompt": [
      "color",
      "sepia",
      "overly cinematic lighting",
      "beauty retouch plastic skin",
      "low resolution",
      "blur",
      "distorted anatomy"
    ]
  }
}