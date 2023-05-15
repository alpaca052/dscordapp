import discord
import requests
import mytoken


def send_line(msg):
    acc_token = mytoken.Line.acc_token
    # サーバーに送るパラメータを用意
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': 'Bearer ' + acc_token}
    payload = {'message': msg}
    requests.post(url, headers=headers, params=payload)

client = discord.Client()


# チャンネル入退室時の通知処理
@client.event
async def on_voice_state_update(member, before, after):

    # チャンネルへの入室ステータスが変更されたとき（ミュートON、OFFに反応しないように分岐）
    if before.channel != after.channel:
        # 通知メッセージを書き込むテキストチャンネル（チャンネルIDを指定）
        #botRoom = client.get_channel(1107478552569462874)

        # 入退室を監視する対象のボイスチャンネル（チャンネルIDを指定）
        announceChannelIds = [mytoken.Discord.voice_channel_token]
        
        ## ラインで通知
        send_line(after.channel.name + "に、" + member.name + "が参加したゾ！")

        # 退室通知
        #if before.channel is not None and before.channel.id in announceChannelIds:
        #    await botRoom.send("**" + before.channel.name + "** から、__" + member.name + "__  が抜けました！")
        # 入室通知
        #if after.channel is not None and after.channel.id in announceChannelIds:
        #    await botRoom.send("**" + after.channel.name + "** に、__" + member.name + "__  が参加したゾ！")

# Botのトークンを指定（デベロッパーサイトで確認可能）
client.run(mytoken.Discord.bot_token)