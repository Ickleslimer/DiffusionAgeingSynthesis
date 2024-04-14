from diffusers import (
    StableDiffusionPipeline,
)
from PIL import Image

text2img = StableDiffusionPipeline.from_pretrained("diffusers\examples\dreambooth\output\pytorch_lora_weights.bin")

device = "cuda"

prompt = "a photo of a dog"

image = text2img(prompt, num_inference_steps=50, guidance_penalty=1.0)
# now you can use text2img(...), img2img(...), inpaint(...) just like the call methods of each respective pipeline
image = Image.fromarray(image["images"][0])
image.save("dog.jpg")