import pyglet


class Window1(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = pyglet.text.Label(
            'Window 1', font_size=36, x=self.width//2, y=self.height//2, anchor_x='center', anchor_y='center')

    def on_draw(self):
        self.clear()
        self.label.draw()


class Window2(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = pyglet.text.Label(
            'Window 2', font_size=36, x=self.width//2, y=self.height//2, anchor_x='center', anchor_y='center')

    def on_draw(self):
        self.clear()
        self.label.draw()


window1 = Window1(width=400, height=400, caption='Window 1')
window2 = Window2(width=400, height=400, caption='Window 2')

pyglet.app.run()
