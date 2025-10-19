from transformers import pipeline


class GenDesc:
def __init__(self, model_name: str = 'google/flan-t5-base'):
self.pipe = pipeline('text2text-generation', model=model_name)


def describe(self, title: str, brand: str, material: str, color: str) -> str:
prompt = (
f"Write a catchy 2-3 sentence product blurb for a furniture item.\n"
f"Item: {title}. Brand: {brand}. Material: {material}. Color: {color}.\n"
f"Tone: modern, warm, benefits-forward."
)
out = self.pipe(prompt, max_new_tokens=96, do_sample=True, temperature=0.8)[0]['generated_text']
return out.strip()
