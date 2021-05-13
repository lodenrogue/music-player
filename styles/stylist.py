STYLES_PATH = 'styles/styles.qss'


class Stylist:

    def get_style_sheet(self):
        with open(STYLES_PATH, 'r') as f:
            return f.read()
