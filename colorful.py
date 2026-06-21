class F:
    @staticmethod
    def color(code):
        """
        Return ANSI escape code for selected color for Foreground.
        :param code:
        :return: string ANSI escape code
        """
        return f"\033[38;5;{code}m"

    @staticmethod
    def reset():
        """
        Return ANSI escape code for default color.
        :return: string ANSI escape code
        """
        return "\033[0m"

class B:
    @staticmethod
    def color(code):
        """
        Return ANSI escape code for selected color for Background.
        :param code:
        :return: string ANSI escape code
        """
        return f"\033[48;5;{code}m"

    @staticmethod
    def reset():
        """
        Return ANSI escape code for default color.
        :return: string ANSI escape code
        """
        return "\033[0m"
