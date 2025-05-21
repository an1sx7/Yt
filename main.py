from flet import *
import yt_dlp
op={
    "format":"best",
}
def main(page:Page):
    page.title="YouTube Dowloader"
    page.window.width=390
    page.window.height=680
    page.window.top=5
    page.window.left=880
    page.horizontal_alignment="center"
    page.vertical_alignment="center"
    inp=TextField(label="vedio link",icon=icons.LINK)

    def down(e):
        url=inp.value
        with yt_dlp.YoutubeDL(op) as y:
            y.download([url])
        txt=Text("dowloaded")
        page.add(txt)
        page.update()

    btn=FilledButton("download",icon=icons.DOWNLOAD,on_click=down,bgcolor=colors.BLUE,color="white")
    page.add(
        AppBar(
            title=Row([
                Text("YouTube Dowloader")
            ],alignment=MainAxisAlignment.CENTER),
            bgcolor=colors.BLUE,
            color="white"
        ),
        inp,btn
    )
    page.update()
app(main)