from . import wizards


banner = """
CrowdStrike Cloud Demo Shell                                          |
                                                  ____________    __ -+-  ____________
This shell-like wizard allows for quick learning, \\_____     /   /_ \\ |   \\     _____/
demoing, and prototyping of cloud operations with  \\_____    \\____/  \\____/    _____/
CrowdStrike Falcon agent.                           \\_____                    _____/
                                                       \\___________  ___________/
Please issue help() to learn more.                               /____\\
"""


python_help = help


def help(item=None):
    text = """
    This is interactive Python shell. Python help is available under python_help()

    This shell has certain items pre-configured for rapid use. The most notable
    items follow.
    """
    if item is None:
        print(text)
        for wizard_klass in wizards.ALL:
            print("\t - wizards.%s" % wizard_klass.__name__)
        print()
        print("    Use help(WizardName) to learn more about each one")
    elif callable(getattr(item, 'help', None)):
        item.help()
    else:
        print(item.__doc__)


def embed():
    from IPython.terminal.embed import InteractiveShellEmbed
    ipshell = InteractiveShellEmbed(banner1=banner)
    ipshell.confirm_exit = False
    ipshell()


embed()
