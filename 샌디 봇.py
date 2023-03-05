import discord
from discord.ext import commands
import youtube_dl



class chatbot(discord.Client):
    # 프로그램이 처음 실행되었을 때 초기 구성
    async def on_ready(self):
        # 상태 메시지 설정
        # 종류는 3가지: Game, Streaming, CustomActivity
        game = discord.Game("내용")

        # 계정 상태를 변경한다.
        # 온라인 상태, game 중으로 설정
        await client.change_presence(status=discord.Status.online, activity=game)

        # 준비가 완료되면 콘솔 창에 "READY!"라고 표시
        print("샌디 대기중")

    # 봇에 메시지가 오면 수행 될 액션
    async def on_message(self, message):
        # SENDER가 BOT일 경우 반응을 하지 않도록 한다.
        if message.author.bot:
            return None
        
        # message.content = message의 내용
        if message.content == "!샌디":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "아이도루다요"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        if message.content == "!가챠":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "샌디~~빔"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        if message.content == "!바보":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "바~~~~~~보"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None
        if message.content == "!앨범":
            # 현재 채널을 받아옴
            channel = message.channel
            # 답변 내용 구성
            msg = "https://www.youtube.com/watch?v=cKmhab15cCc"
            # msg에 지정된 내용대로 메시지를 전송
            await channel.send(msg)
            return None


# 프로그램이 실행되면 제일 처음으로 실행되는 함수
if __name__ == "__main__":
    # 객체를 생성
    client = chatbot(intents=discord.Intents.all())
    # TOKEN 값을 통해 로그인하고 봇을 실행
    client.run("MTA4MTU4NzE2NzYwMTYzNTQyOA.GS8rdE.b8V0ccQILg4WX6LdgSbssBE5byrATgwQTIpeF8")