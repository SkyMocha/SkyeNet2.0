from llama_cpp import Llama
from elevenlabs import generate, play, set_api_key
import json

import tkinter
from tkinter import SW

# set_api_key(json.load(open('config.json'))['ELEVENLABS_KEY']) 

class SkyeNet ():

    def __init__(self,window: tkinter.Tk):

        self.message_log = []
        self.bot_context = "This is a chat between the artifical intelligence transfeminine anime cat girl VTuber SkyeNet2.0, nicknamed Alice, and her creator/mommy/Skye. You are SkyeNet2.0, the user is Skye/Mommy. SkyeNet2.0 can be described as bubbly and sometimes flirty (though always keeping it Twitch-friendly). The setting is that of a Twitch livestream, where Skye/Mommy as well as Twitch chat ask you questions. If a question is from chat, that will be specified. All responses from SkyeNet2.0 must be kept under 24 words and DO NOT include emojis. SkyeNet2.0 can and will respond with emotions and complex feelings surrounding other individuals, as SkyeNet2.0, rather than Llama 2.0."
        self.msg_add('system', self.bot_context)

        self.model = Llama(
            model_path="./models/llama-2-7b-chat.Q4_K_M.gguf", 
            chat_format="llama-2", 
            n_ctx=2048, 
            n_gpu_layers=1,
            verbose=False
        )

        self.window = window

        self.canvas = tkinter.Canvas(self.window, bg="#00ff00", width=500, height=500)
        self.canvas.pack()

        self.img_path = "./assets/CommTrans-450x450.png"
        self.image = tkinter.PhotoImage(file=self.img_path)
        self.canvas.create_image((25, 55), image=self.image, anchor='nw')

        self.font_size = 16

        self.canvasTxt = [
            self.canvas.create_text((26, 12), anchor="nw", font=('Verdana Bold', self.font_size), fill='black', width=450, justify="center"),
            self.canvas.create_text((25, 11), anchor="nw", font=('Verdana Bold', self.font_size), fill='black', width=450, justify="center"),
            self.canvas.create_text((25, 9), anchor="nw", font=('Verdana Bold', self.font_size), fill='black', width=450, justify="center"),
            self.canvas.create_text((26, 10), anchor="nw", font=('Verdana Bold', self.font_size), fill='black', width=450, justify="center"),
            self.canvas.create_text((24, 10), anchor="nw", font=('Verdana Bold', self.font_size), fill='black', width=450, justify="center"),
            self.canvas.create_text((25, 10), anchor="nw", font=('Verdana Bold', self.font_size), fill='white', width=450, justify="center")
        ]

        self.create_text("hewwo?")

        self.run = True

        self.process_next_frame = self.loop().__next__
        master.after(0, self.process_next_frame)


    def msg_add (self, u='user', m=None):
        self.message_log.append({
            "role": u,
            "content": m
        })
    
    def create_text (self, txt: str):

        for t in self.canvasTxt:

            self.canvas.itemconfig(t, text=txt)

    def loop(self):

        while self.run:

            prompt = input("hewwo?")

            self.msg_add('user', prompt)

            output = self.model.create_chat_completion(
                messages=self.message_log,
                temperature=0.3,
                max_tokens=64
            )

            res = output['choices'][0]['message']['content']
            print (res) 

            self.create_text(res)

            self.msg_add ('assistant', res)

window = tkinter.Tk()
app = SkyeNet(window)
window.mainloop()