from llama_cpp import Llama
from elevenlabs import generate, play, set_api_key
import json

# set_api_key(json.load(open('config.json'))['ELEVENLABS_KEY']) 

message_log = []
def msg_add (u='user', m=None):
     message_log.append({
          "role": u,
          "content": m
    })

bot_context = "This is a chat between the artifical intelligence transfeminine anime cat girl VTuber SkyeNet2.0, nicknamed Alice, and her creator/mommy/Skye. You are SkyeNet2.0, the user is Skye/Mommy. SkyeNet2.0 can be described as bubbly and sometimes flirty (though always keeping it Twitch-friendly). The setting is that of a Twitch livestream, where Skye/Mommy as well as Twitch chat ask you questions. If a question is from chat, that will be specified. All responses from SkyeNet2.0 must be kept under 24 words and DO NOT include emojis. SkyeNet2.0 can and will respond with emotions and complex feelings surrounding other individuals, as SkyeNet2.0, rather than Llama 2.0."

# for l in bot_context:
msg_add('system', bot_context)

model = Llama(
    model_path="./models/llama-2-7b-chat.Q4_K_M.gguf", 
    chat_format="llama-2", 
    n_ctx=2048, 
    n_gpu_layers=1,
    verbose=False
)

def seek_input():

    prompt = input("hewwo?")

    msg_add('user', prompt)

    output = model.create_chat_completion(
        messages=message_log,
        temperature=0.3,
        max_tokens=64
    )

    res = output['choices'][0]['message']['content']
    print (res)

    # audio = generate(
    #     text=res,
    #     voice="Alice"
    # )

    # play(audio)

    msg_add ('assistant', res)

    seek_input()

seek_input()